import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from dotenv import load_dotenv

# Model Imports
from models import User as ModelUser
from models import Item as ModelItem

# Schema Imports
from schema import User as SchemaUser
from schema import Item as SchemaItem

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR,'.env'))

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    root_path='/api/v1'
)

app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ['DATABASE_URL'])

# arbitrary user resource I built when following a tutorial - not used in streamlit CRUD example
@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age)
    db.session.add(db_user)
    db.session.commit()
    return db_user

# create an item
@app.post("/item/", response_model=SchemaItem)
def create_item(item: SchemaItem):
    db_item = ModelItem(
        name=item.name,
        price=item.price)
    db.session.add(db_item)
    db.session.commit()
    return db_item

# update an existing item
@app.post("/item/{id}", response_model=SchemaItem)
def create_item(id: int, item: SchemaItem):
    db_item = db.session.query(ModelItem).filter(ModelItem.id == id).first()
    db_item.name = item.name
    db_item.price = item.price
    db.session.commit()
    return db_item

# get all items
@app.get('/items/')
def get_items():
    db_items = db.session.query(ModelItem).all()
    return db_items
    # return 'all items lol'

@app.get('/')
def test():
    return 'Yes this test worked!'

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)