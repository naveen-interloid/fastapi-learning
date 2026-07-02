from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Book(Base):
    __tablename__= 'allbooks'
    
    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    
    bookname : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    user_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable = False
    )
    
    user: Mapped['User'] = relationship(
        'User',
        back_populates='books'
    )