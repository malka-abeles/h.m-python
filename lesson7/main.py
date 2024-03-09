# from fastapi import FastAPI
import uvicorn
import fastapi
# from pydantic import BaseModel
import pydantic

app = fastapi.FastAPI()


class Task(pydantic.BaseModel):
    id: int
    name: constr(minlength=1, maxlength=30)
    description: str
    status: bool


task = Task(id=1, name="malka", description="to do h.m", status=False)

tasks =[task]

@app.get('/')
async def get():
    return tasks

@app.post('/')
async def post(task: Task):
    try:
        tasks.append(task)
    except ValidationError:
        raise pydantic.HTTPException(status_code=400, detail="oops... an error occurred")
    return tasks


@app.put('/')
async def put(task: Task):
    for idx, t in enumerate(tasks):
        if t.id == task.id:
            try:
                tasks[idx] = task
            except:
                raise pydantic.HTTPException(status_code=400, detail="oops... an error occurred")
    return tasks


@app.delete('/')
async def delete(id: int):
    for s in tasks:
        if (s.id == id):
            try:
                tasks.remove(s)
            except:
                raise pydantic.HTTPException(status_code=400, detail="oops... an error occurred")
    return tasks
