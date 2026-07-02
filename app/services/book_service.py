from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.book_model import Book
from app.models.user_model import User
from app.schemas.book_schema import BookCreate


def create_book(
    db:Session,
    book_data : BookCreate
):    
    user = db.query(User).filter(
        User.id == book_data.user_id
    ).first()
    
    if user is None : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    
    existing = db.query(Book).filter(
        Book.bookname == book_data.bookname,
        Book.user_id == book_data.user_id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Book already exists for this user'
        )
    
    book = Book(
        bookname = book_data.bookname,
        user_id = book_data.user_id
    )
    try:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book
    except IntegrityError :
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Database integrity error'
        )
    