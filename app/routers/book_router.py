from fastapi import APIRouter, Depends, status

from app.database.database import get_db
from app.schemas.book_schema import BookCreate, BookResponse
from app.services.book_service import create_book

router = APIRouter(
    prefix='/book',
    tags=['Books']
)


@router.post(
    '/',
    response_model = BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_book(
    book_data : BookCreate,
    db = Depends(get_db)
):
    return create_book(
        db = db,
        book_data = book_data
    )
