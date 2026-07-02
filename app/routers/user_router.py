from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.book_schema import BookResponse
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services.user_service import (
    create_user,
    delete_user,
    get_user,
    get_user_allbooks,
    get_users,
    modify_user,
)

router = APIRouter(
    prefix='/user',
    tags=["Users"]
)

@router.post(
    '/',
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_user(
    user_data:UserCreate,
    db:Session = Depends(get_db)
):
    
    return create_user (
        db = db,
        user_data = user_data
    )


@router.get(
    '/',
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK
)
def read_users(
    username: str | None = None,
    email : str | None = None,
    page : int = Query(default = 1, ge = 1),
    limit : int = Query(default = 5, ge = 1 , le = 100 ),
    db:Session = Depends(get_db)
):
    return get_users(
        db = db , 
        username= username,
        email = email,
    )


@router.get(
    '/{user_id}',
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
def read_user(
    user_id:int,
    db:Session = Depends(get_db)
):
    
    return get_user(
        db = db,
        user_id = user_id
    )


@router.put (
    '/{user_id}',
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
def update_user (
    user_id:int,
    user_data : UserUpdate,
    db:Session = Depends(get_db)
):
    
    return modify_user(
        db = db , 
        user_id = user_id,
        user_data = user_data
    )



@router.delete (
    '/{user_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
def del_user (
    user_id:int,
    db:Session = Depends(get_db)
):
    
    delete_user(
        db = db , 
        user_id = user_id
    )
    
    
    
    
@router.get(
    '/{user_id}/books',
    response_model=list[BookResponse],
    status_code=status.HTTP_200_OK
)
def get_user_books(
    user_id : int,
    db : Session = Depends(get_db),
):
    return get_user_allbooks(
        db = db,
        user_id = user_id,
    )