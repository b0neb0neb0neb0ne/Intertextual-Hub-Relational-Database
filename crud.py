from sqlalchemy.orm import Session

from . import models, schemas


def get_result(db: Session, user_id: int):
    return db.query(models.Compilation).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Compilation).first()


#def create_entry(db: Session, user: schemas.UserCreate):
#    fake_hashed_password = user.password + "notreallyhashed"
#    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#    db.add(db_user)
#    db.commit()
#    db.refresh(db_user)
#    return db_user
