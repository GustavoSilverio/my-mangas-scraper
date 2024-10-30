from models.manga import Manga
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("MONGO_BASE_URL"))
db = client["my-mangas"]
collection = db["manga"]


def salvarManga(manga: Manga):
    result = collection.insert_one({
        "nome": manga.get("nomeManga"),
        "capitulos": manga.get("capitulos"),
        "imgCapa": manga.get("imgCapa")
    })
    print("Id mangá: ", result.inserted_id)