from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()


# GET
# POST
# PUT
# DELETE
# PATCH
# HEAD
# OPTIONS

lista_items = {1: 'Item 1', 2: 'Item 2', 3: 'Item 3'}

# METODO PARA MOSTRAR UN ITEM ESPECIFICO
@app.get("/items/{id_item}")
async def show_item_name(id_item: int):
    return lista_items[id_item]

# METODO PARA MOSTRAR TODOS LOS ITEMS
@app.get("/items")
async def show_item_name():
    return lista_items

# METODO PARA AGREGAR
@app.post("/items")
async def add_item(value: str):
    cantidad = len(lista_items) + 1
    lista_items[cantidad] = value;
    return "Se agrego el item al diccionario"

# METODO PARA ACTUALIZAR
@app.put("/items/{id_item}")
async def update_item(id_item: int, new_value: str):
    lista_items[id_item] = new_value
    return "Valor Actualizado"

# METODO PARA ELIMIAR UN ITEM
@app.delete("/items/{id_item}")
async def delete_item(id_item: int):
    del lista_items[id_item]
    return "El item ha sido eliminado"