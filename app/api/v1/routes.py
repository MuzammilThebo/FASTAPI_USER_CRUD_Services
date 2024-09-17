from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import create_user, get_user, update_user, deactivate_user
from app.schemas.user import UserCreate, UserUpdate
from app.db.session import get_db

router = APIRouter()

@router.post("/create_user/")
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, username=user.username, password=user.password)

@router.get("/get_user/{username}")
def get_user_route(username: str, db: Session = Depends(get_db)):
    user = get_user(db, username=username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/update_user/")
def update_user_route(user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, username=user.username, password=user.password)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/deactivate_user/{username}")
def deactivate_user_route(username: str, db: Session = Depends(get_db)):
    user = deactivate_user(db, username=username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deactivated"}
