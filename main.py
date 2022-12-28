# -*- coding: utf-8 -*-
# cd /d D:\vscode\fastapi
# https://1mu6oq.deta.dev
# pip install -r requirements.txt
# uvicorn main:app --reload
import db
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello Japan"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/news")
def get_news_list():
    sql = "select * from news limit 10"
    ret = db.get_data(sql)
    return ret