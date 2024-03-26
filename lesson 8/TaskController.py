from http.client import HTTPException
from fastapi import FastAPI, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum

from pydantic import BaseModel, constr, field_validator, ValidationError

tasks_router = APIRouter()

Tasks = {}


class StatusEnum(str, Enum):
    open = 'open'
    close = 'close'


class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z_]+$")
    Des: str
    id: int
    status: StatusEnum

    @field_validator('Des')
    def check_Des(cls, Des):
        if len(Des) > 100:
            raise ValueError('error')
        return Des

    @field_validator('id')
    def check_Des(cls, id):
        if id > 100:
            raise ValueError('error')
        return id


@tasks_router.get("/")
async def task():
    return Tasks
    raise HTTPException(status_code=404, detail="oops... your task didn't find")


@tasks_router.post("/")
async def add_task(task: Task):
    try:
        Tasks[task.id] = task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@tasks_router.put("/{id}", response_model=Task)
async def update_task(id: int, item: Task):
    update_item_encoded = jsonable_encoder(item)
    Tasks[id] = update_item_encoded
    return update_item_encoded


@tasks_router.delete("/{id}")
async def delete_task(id: int):
    del Tasks[id]
    return {"message": "Item deleted"}

#
# def other_func(name: str):
#     return name == "sara"

#
# @example_router.get("/all")
# async def get_user(is_authenticated: bool = Depends(other_func)):
#     if is_authenticated:
#         return "great"
