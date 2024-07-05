from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List, Dict, Union, Optional
from database.userservice import *
import re


def phone_number_checker(phone):
    regex = re.compile(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
    if re.fullmatch(regex, phone):
        return True
    return False


class User(BaseModel):
    name: str
    phone: str
    user_location: str
    tg_id: int | None = None


users_router = APIRouter(tags=["Управление юзерами"], prefix="/users")


@users_router.post("/api/registration")
async def registration_user(user_model: User):
    user_data = dict(user_model)
    phone_number_validation = phone_number_checker(user_model.phone)
    if phone_number_validation:
        try:
            reg_user = register_user_db(**user_data)
            return {"status": 1, "message": reg_user}
        except Exception as e:
            return {"status": 0, "message": e}
    return {"status": 0, "message": "Invalid phone"}


@users_router.post("/api/check_user")
async def check_user(tg_id: int):
    exact_user = check_user_db(tg_id)
    if exact_user:
        return {"status": 1, "message": True}
    return {"status": 0, "message": False}


@users_router.get("/api/user/{user_id}")
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)
    if exact_user:
        return {"status": 1, "message": exact_user}
    return {"status": 0, "message": "Пользователь не найден"}


@users_router.get("/api/user")
async def get_all_users():
    all_users = get_all_users_db()
    if all_users:
        return {"status": 1, "message": all_users}
    return {"status": 0, "message": "Пользователи не найдены"}


@users_router.put("/api/change_profile")
async def change_user_profile(user_id: int, changeable_info: str, new_data: str):
    data = change_user_data_db(user_id=user_id, changeable_info=changeable_info, new_data=new_data)
    if data:
        return {"status": 1, "message": "Данные пользователя успешно изменены"}
    return {"status": 0, "message": "Не удалось изменить информацию"}

