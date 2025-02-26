from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI ()

class User(BaseModel):
    id: int
    nombre : str
    apellido: str
    edad: int

users_list = [User(id=1, nombre = "Gabriel",apellido = "borges", edad =44),
              User(id=2,nombre="julieta",apellido="rodriguez",edad=22),
              User(id=3,nombre="nicole",apellido="colmenares", edad=33)]


@app.get ("/usersjson")
def usersjson():
    return [{"nombre" : "Gabriel", "apellido" : "borges", "edad" : 44},
            {"nombre" : "julieta", "apellido" : "rodriguez", "edad" : 22},
            {"nombre" : "nicole", "apellido" : "colmenares", "edad" : 33}]

@app.get ("/users")
def users():
    return users_list

#path
@app.get ("/user/{id}")
def user(id: int):
    return search_user(id)

#query
@app.get ("/userquery/")
def user(id: int):
    return search_user(id)

#/calculadora?numero_1=3&numero_2=3
@app.get ("/calculadora")
def calcular(numero_1 : float , numero_2 : float):
    return {"suma" : numero_1 + numero_2}


def search_user(id:int):
    users = filter (lambda user : user.id == id,users_list)
    try:
        return list(users)[0]
    except:
        return {"ERROR" : "NO SE HA ENCONTRADO AL USUARIO"}
    


@app.post("/user/")
def user (user : User):
    if type(search_user(user.id)) == User:
        return {"ERROR" : "EL USUARIO YA EXISTE"}
    else:
        users_list.append (user)
        return user 

@app.put("/user/")
def user (user : User):
    found = False
    for index, saved_user in enumerate (users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"ERROR" : "NO SE HA ACTUALIZADO EL USUARIO"}
    else: 
        return user 


@app.delete ("/user/{id}")
def user(id: int):
    found = False
    for index, saved_user in enumerate (users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"ERROR" : "NO SE HA ELIMINADO EL USUARIO"}
    





#@app.get ("/")
#def saludo():
#    return "holllaa"


#@app.get ("/url")
#def url():
#    return {"url" : "https://www.twitch.tv/"}

