from scrapers import mangaOnline, slimeRead
from models.manga import Manga
from urllib.parse import urlparse
from typing import Dict, Callable

sites: Dict[str, Callable[[str], Manga]] = {
    "mangaonline.biz": mangaOnline.obterManga,
    "slimeread.com": slimeRead.obterManga,
}

def fazerWebScrapping(url: str) -> Manga:
    parsed_url = urlparse(url)
    dominio = parsed_url.netloc
    
    for dominio_site, obterManga in sites.items():
        if dominio_site in dominio:
            return obterManga(url)
        
    raise ValueError(f"Domínio {dominio} não suportado.")