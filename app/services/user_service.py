from app.models.user import User
from sqlalchemy.orm import Session
from app.utils.hashing import get_password_hash, verify_password

def create_user(db: Session, username: str, password: str):
    hashed_password = get_password_hash(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def update_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if user:
        user.password = get_password_hash(password)
        db.commit()
        return user
    return None

def deactivate_user(db: Session, username: str):
    user = get_user(db, username)
    if user:
        user.active = False
        db.commit()
        return user
    return None
