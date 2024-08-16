import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urlparse

def obterCapitulos(nome_manga: str):
    # obter lista de capítulos do manga
    result_capitulos = requests.get(nome_manga)

    if result_capitulos.status_code != 200:
        print("Página do mangá não encontrada!")

    soup_capitulos = BeautifulSoup(result_capitulos.text, "html.parser")

    lista_capitulos_html = soup_capitulos.find_all("div", class_="episodiotitle")

    lista_links_capitulos : List[str] = [] 

    for cap in lista_capitulos_html:
        if cap.a['href']:
            lista_links_capitulos.append(cap.a['href'])
        else:
            print("Capitulo sem link!")

    print("Capítulos encontrados: ", len(lista_links_capitulos))

    # obter cada página de cada capítulo

    lista_capitulos : List[List[str]] = []
    lista_paginas : List[str] = []
    contador_capitulos = 1
    contador_paginas = 1
    contador_erros = 0

    for link_cap in reversed(lista_links_capitulos): # reversed pois os capitulos começam do último
        
        result_capitulo = requests.get(link_cap)
        
        if result_capitulo.status_code != 200:
            print("Página do capítulo não encontrada!")
            continue
        
        else:
            soup_capitulo = BeautifulSoup(result_capitulo.text, "html.parser")
            paginas = soup_capitulo.find("div", class_="content").find_all("p")[1:-1]
            
            for p in paginas:
                    if p.img and "src" in p.img.attrs:
                        lista_paginas.append(p.img["src"])
                        contador_paginas += 1
                    else:
                        contador_erros += 1
                        lista_paginas.append(None)
                        
            
            parsed_url_capitulo = urlparse(link_cap).path
            numero_capitulo = parsed_url_capitulo.split("/")[-2].split("capitulo")[-1][1:].replace("-", ".")
            
            lista_capitulos.append({
                    "nomeCapitulo": f"Capítulo {numero_capitulo}",
                    "paginas": lista_paginas
                })
            
            contador_capitulos += 1
            contador_paginas = 1
            lista_paginas = []
    
    nome_manga = soup_capitulos.title.text.split(" - ")[0]
    
    print("Páginas não encontradas: ", contador_erros)
    return lista_capitulos, nome_manga