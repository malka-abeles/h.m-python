import pkg_resources
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from starlette.responses import HTMLResponse
from TaskController import tasks_router
from UserController import user_router
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'])
app.include_router(tasks_router, prefix='/Task')
app.include_router(user_router, prefix='/User')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/static", include_in_schema=False)
def root():
    return HTMLResponse(pkg_resources.resource_string(__name__, "static/static.html"))

@app.on_event('startup')
async def print_something():
    print("something")




if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")

