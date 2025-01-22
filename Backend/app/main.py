# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from crud import get_users, get_roles
from database import get_db
from models import Users, Roles
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users", response_model=list[Users],tags=["Получить всех пользователей"], summary="Вывод пользователей")
async def read_users(db: Session = Depends(get_db)):
    """
    Информация о модели:

    - **id**:        уникальный номер пользователя в БД
    - **last_name**: фамилия
    - **name**:      имя
    - **e-mail**:    электронная почта
    - **phone**:     номер телефона
    """
    users = get_users(db)
    return users

@app.get("/roles", response_model=list[Roles],tags=["Получить все роли"], summary="Вывод ролей")
def read_roles(db: Session = Depends(get_db)):
    """
    Информация о модели:

    - **id**:          уникальный номер роли в БД
    - **name**:        Название роли
    - **user**:        Объект пользователя
    - **description**: Описание роли
    """
    roles = get_roles(db)
    return roles