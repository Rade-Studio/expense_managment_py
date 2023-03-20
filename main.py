from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(defailt=None, alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results