from typing import List, TypedDict

class Capitulo(TypedDict):
    nomeCapitulo: str
    paginas: List[str]

class Manga(TypedDict):
    nomeManga: str
    imgCapa: str
    capitulos: List[Capitulo]
    