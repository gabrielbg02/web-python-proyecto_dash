from controller.user import User
from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model.handle_db import HandleDB


app = FastAPI()

template = Jinja2Templates(directory="./view")



@app.get("/", response_class=HTMLResponse)
def root (req: Request):
    return template.TemplateResponse("index.html" , {"request" : req})

@app.get("/signup", response_class=HTMLResponse)
def signup(req : Request):
    return template.TemplateResponse("signup.html" , {"request" : req})

@app.get ("/user", response_class=HTMLResponse)
def user(req : Request):
    return template.TemplateResponse("user.html",{"request" : req})


@app.post("/data-processing")
def data_processing(firstname : str = Form(), lastname : str = Form(), username : str = Form(), country : str = Form(), password_user : str = Form()):
    data_user = {
        "firstname" : firstname,
        "lastname" : lastname,
        "username" : username,
        "country" : country,
        "password_user" : password_user 
    }
    db = User(data_user)
    db.create_user()
    return {"hola" : "listo"}



