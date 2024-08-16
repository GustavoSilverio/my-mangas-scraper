import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

def obterCapitulos(url_manga: str):
   
    # obter cada página de cada capítulo
    
    def obterPaginasDoCapitulo(link_capitulo: str):
        result_capitulo = requests.get(link_capitulo)
        if result_capitulo.status_code != 200:
            return None
        
        soup_capitulo = BeautifulSoup(result_capitulo.text, "html.parser")
        paginas = soup_capitulo.find("div", class_="content").find_all("p")[1:-1]
        lista_paginas = [p.img["src"] for p in paginas if p.img and "src" in p.img.attrs]
        
        parsed_url_capitulo = urlparse(link_capitulo).path
        numero_capitulo = parsed_url_capitulo.split("/")[-2].split("capitulo")[-1][1:].replace("-", ".")
        capitulo_manga = f"Capítulo {numero_capitulo}"
        
        return lista_paginas, capitulo_manga
    
    
    # obter lista de capítulos do manga
    
    result_capitulos = requests.get(url_manga)
    if result_capitulos.status_code != 200:
        print("Página do mangá não encontrada!")
        return [], ""

    soup_capitulos = BeautifulSoup(result_capitulos.text, "html.parser")
    lista_capitulos_html = soup_capitulos.find_all("div", class_="episodiotitle")
    lista_links_capitulos = [cap.a['href'] for cap in lista_capitulos_html if cap.a['href']]
    print("Capítulos encontrados: ", len(lista_links_capitulos))

    with ThreadPoolExecutor() as executor:
        lista_capitulos = []

        pools = [executor.submit(obterPaginasDoCapitulo, link_cap) for link_cap in lista_links_capitulos]
        
        for pool in pools:
            paginas, nome_capitulo  = pool.result()
            if paginas and nome_capitulo is not None:
                lista_capitulos.append({
                    "nomeCapitulo": nome_capitulo,
                    "paginas": paginas
                })

    nome_manga = soup_capitulos.title.text.split(" - ")[0]
    print("Páginas não encontradas: ", sum(1 for res in lista_capitulos if res is None))
    
    return lista_capitulos, nome_manga