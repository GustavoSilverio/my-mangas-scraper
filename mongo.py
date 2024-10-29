from models.manga import Manga
from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_BASE_URL"))
db = client["my-mangas"]
collection = db["manga"]


def salvarManga(manga: Manga):
    result = collection.insert_one({"nome": manga.get("nomeManga"), "capitulos": manga.get("capitulos")})
    print("Id mangá: ", result.inserted_id)