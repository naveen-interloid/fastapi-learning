from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate


def create_user(db: Session, user_data: UserCreate):
    
    existing = db.query(User).filter(User.email == user_data.email).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,detail="Email exists"
        )

    user = User(
        username=user_data.username,email=user_data.email, password=user_data.password
    )
        
    try :
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Email already exists"
    )
        


def get_users(db: Session,username : str | None = None,email : str | None = None, page: int = 1,limit: int = 10):
    
    offset = (page - 1) * limit
    
    query = db.query(User)
    
    if username is not None:
        query = query.filter(User.username == username)
    
    if email is not None:
        query = query.filter(User.email == email)
    
    query = query.offset(offset).limit(limit)
    
    return query.all()


def get_user(db: Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def modify_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    user.username = user_data.username
    user.email = user_data.email

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db.delete(user)
    db.commit()
    
    
def get_user_allbooks(
    db : Session,
    user_id
):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )
    return user.books