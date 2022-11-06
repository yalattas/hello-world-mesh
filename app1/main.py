from typing import Union
from fastapi import FastAPI
import requests
import json
import os, uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "health":True,
    }

@app.get("/call")
def read_root():
    try:
        response = requests.get('http://app2_service:8001/sample').text
        response = json.loads(response)
    except KeyError as e:
        print('error in network layer: ', e)
    return {
        "first function":"here I am",
        "Hello": response['function']
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=int(os.environ.get('APP_PORT', default=8000)), reload=True)