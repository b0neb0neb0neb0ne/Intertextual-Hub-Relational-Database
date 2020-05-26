from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
# i don't think i need the relationship import statement

from .database import Base


class Compilation(Base):
    __tablename__ = "test"

    author = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(DateTime)
    philo_id = Column(String, default=True)

