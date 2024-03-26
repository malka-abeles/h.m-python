from http.client import HTTPException
from fastapi import FastAPI, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, constr, field_validator, ValidationError

user_router = APIRouter()

Users = {}


class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z_]+$")
    id: int

    @field_validator('id')
    def check_Des(cls, id):
        if id > 100:
            raise ValueError('error')
        return id


def check(name: str):
    return name == "111"


@user_router.get("/")
async def user(is_authenticated: bool = Depends(check)):
    if (is_authenticated):
        return Users
    else:
        raise HTTPException(status_code=404, detail="oops... your user didn't find")


@user_router.post("/")
async def add_user(user: User):
    try:
        Users[user.id] = user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"


@user_router.put("/{id}", response_model=User)
async def update_user(id: int, item: User):
    update_item_encoded = jsonable_encoder(item)
    Users[id] = update_item_encoded
    return update_item_encoded


@user_router.delete("/{id}")
async def delete_user(id: int):
    del Users[id]
    return {"message": "Item deleted"}

#
# def other_func(name: str):
#     return name == "sara"

#
# @example_router.get("/all")
# async def get_user(is_authenticated: bool = Depends(other_func)):
#     if is_authenticated:
#         return "great"
