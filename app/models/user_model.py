from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class User(Base):
    __tablename__= 'users'
    
    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    
    username : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
        
    email : Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    
    password : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    books: Mapped[list['Book']] = relationship(
        'Book',
        back_populates='user',
        cascade='all,delete-orphan'
    )

