import sys

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette import status
from pydantic import BaseModel
from .auth import get_password_hash, get_current_user
from .utils import verify_password
import models
from database import SessionLocal, engine

sys.path.append("..")

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {'description': 'Not found'}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    email: str
    password: str
    password_new: str


@router.get("/edit-password", response_class=HTMLResponse)
async def edit_password(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/auth, status_code=status.HTTP_302_FOUND")
    return templates.TemplateResponse("edit-user-password.html", {"request": request, "user": user})


@router.post("/edit-password", response_class=HTMLResponse)
async def user_password_change(
        request: Request, username: str = Form(...),
        password: str = Form(...),
        password_new: str = Form(...),
        db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)
    user_data = db.query(models.Users).filter(
        models.Users.username == username).first()
    msg = "Неправильное имя пользователя или пароль"
    if user_data is not None:
        if username == user_data.username and verify_password(password, user_data.hashed_password):
            user_data.hashed_password = get_password_hash(password_new)
            db.add(user_data)
            db.commit()
            msg = "Пароль успешно изменен"
    return templates.TemplateResponse(
        "edit-user-password.html",
        {"request": request, "user": user, "msg": msg})
