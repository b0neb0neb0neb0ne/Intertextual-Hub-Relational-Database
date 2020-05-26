from typing import List
from datetime import date

from pydantic import BaseModel

class RowBase(BaseModel):
    author: str
    title: str
    year: date
    philo_id: str  

class RowCreate(RowBase):
    pass

class Row(RowBase):
    author: str
    title: str
    year: date
    philo_id: str  

    class Config:
        orm_mode = True
