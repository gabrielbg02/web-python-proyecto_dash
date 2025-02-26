from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

app = FastAPI ()

class Producto(BaseModel):
    id: Optional[str] = None
    nombre : str
    apellido: str
    edad: int

lista_productos = []


@app.get ("/")
def bienvenido():
    return {"bienvenido" : "hola"}

@app.get("/producto")
def mostrar_producto():
    return lista_productos

@app.post("/producto")
def crear_producto(producto : Producto):
    producto.id = str (uuid())
    lista_productos.append (producto)
    return {"mensaje" : "agregado"}


@app.get ("/producto/{producto_id}")
def buscar_producto(producto_id : str):
    resultado = list (filter (lambda p: p.id == producto_id, lista_productos))
    if len (resultado):
        return resultado[0]
    
    #return {"mensaje" : f"el producto con el ID {producto_id} no fue encontrado"} 
    raise HTTPException (status_code=404, detail= f"el producto con el ID {producto_id} no fue encontrado")


@app.delete("/producto/{producto_id}")
def eliminar_producto(producto_id : str):
    resultado = list (filter (lambda p: p.id == producto_id, lista_productos))
    if len (resultado):
        producto = resultado[0]
        lista_productos.remove (producto)
        return {"producto" : "eliminado correctamente"}
    #return {"mensaje" : f"el producto con el ID {producto_id} no fue encontrado"} 
    raise HTTPException (status_code=404, detail= f"el producto con el ID {producto_id} no fue eliminado")

@app.put("/producto/{producto_id}")
def actualizar_producto(producto_id : str, producto : Producto):
    resultado = list (filter (lambda p: p.id == producto_id, lista_productos))
    if len (resultado):
        producto_encontrado = resultado[0]
        producto_encontrado.nombre = producto.nombre
        producto_encontrado.apellido = producto.apellido
        producto_encontrado.edad = producto.edad
        return producto_encontrado
    
    raise HTTPException (status_code=404, detail= f"el producto con el ID {producto_id} no fue encontrado")


#for p in lista_productos:
#      if p.id == producto_id:
#         return p