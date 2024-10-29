from typing import List, TypedDict

class Capitulo(TypedDict):
    nomeCapitulo: str
    paginas: List[str]

class Manga(TypedDict):
    capitulos: List[Capitulo]
    nomeManga: str
    