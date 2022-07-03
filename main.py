import functions
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Sign In.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    return templates.TemplateResponse("Search.html", {"request": request})


@app.get("/new-entry", response_class=HTMLResponse)
async def new_entry(request: Request):
    return templates.TemplateResponse("Enter New.html", {"request": request})


@app.post("/login")
async def login(request: Request):
    credentials = await request.json()
    message = functions.authenticate(credentials)
    return message

@app.post("/parameters")
async def parameters(request: Request):
    credentials = await request.json()
    message = functions.writeparameters(credentials)
    return message

@app.post("/new-user")
async def new_user(username: str, password: str):
    message = functions.new_user(username, password)
    return message
