from typing import Union
from fastapi import FastAPI
import os, uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"health": True}

@app.get("/sample")
def read_root():
    return {"function": "hello from function 2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=int(os.environ.get('APP_PORT', default=8001)), reload=True)