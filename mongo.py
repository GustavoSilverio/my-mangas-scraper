from typing import List, Dict
from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_BASE_URL"))
db = client["my-mangas"]
collection = db["manga"]


def salvarManga(capitulos: List[Dict[str, List[Dict[str, str]]]], nome_manga: str):
    result = collection.insert_one({"nome": nome_manga, "capitulos": capitulos})
    print("Id mangá: ", result.inserted_id)