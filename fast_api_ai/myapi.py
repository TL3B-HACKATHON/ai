from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = {'itching': 1, 'skin_rash': 1}

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post("/items/")
def create_item(item: Item):
    return item

class DataModel(BaseModel):
    texts:str

@app.post("/send_greetings")
async def send_data(text: DataModel):
    print(text.texts)
    return {"achraf":"taffah"}

