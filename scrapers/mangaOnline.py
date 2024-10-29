import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from models.manga import Capitulo, Manga
from typing import List

# obter cada página de capítulo específico
    
def obterPaginasDoCapitulo(link_capitulo: str):
    result_capitulo = requests.get(link_capitulo)
    if result_capitulo.status_code != 200:
        return None
    
    soup_capitulo = BeautifulSoup(result_capitulo.text, "html.parser")
    paragrafos = soup_capitulo.find("div", class_="content").find_all("p")[1:-1]
    paginas: List[str] = [p.img["src"] for p in paragrafos if p.img and "src" in p.img.attrs]
    
    parsed_url_capitulo = urlparse(link_capitulo).path
    numero_capitulo = parsed_url_capitulo.split("/")[-2].split("capitulo")[-1][1:].replace("-", ".")
    nome_capitulo = f"Capítulo {numero_capitulo}"
    
    return paginas, nome_capitulo


# obter lista de capítulos do manga

def obterManga(url: str) -> Manga:
    result_capitulos = requests.get(url)
    if result_capitulos.status_code != 200:
        raise ValueError(f"Página do mangá não encontrada, Url: {url}")

    soup_capitulos = BeautifulSoup(result_capitulos.text, "html.parser")
    lista_capitulos_html = soup_capitulos.find_all("div", class_="episodiotitle")
    lista_links_capitulos = [cap.a['href'] for cap in lista_capitulos_html if cap.a['href']]

    # obter cada página de cada capítulo com threading

    with ThreadPoolExecutor() as executor:
        capitulos: List[Capitulo] = []

        pools = [executor.submit(obterPaginasDoCapitulo, link_cap) for link_cap in reversed(lista_links_capitulos)]
        
        for pool in pools:
            paginas, nome_capitulo  = pool.result()
            if paginas and nome_capitulo is not None:
                capitulos.append({
                    "nomeCapitulo": nome_capitulo,
                    "paginas": paginas
                })

    nome_manga = soup_capitulos.title.text.split(" - ")[0]
    print("Páginas não encontradas: ", sum(1 for res in capitulos if res is None))
    
    manga: Manga = {
        "capitulos": capitulos,
        "nomeManga": nome_manga,
    }
    
    return manga