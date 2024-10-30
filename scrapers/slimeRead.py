from models.manga import Manga, Capitulo
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from typing import List

def obterPaginasCapitulos(urls: List[str]):
    try:
        driverCapitulo = webdriver.Chrome()
        
        capitulos: List[Capitulo] = []
        
        
        primeira_iteracao = True
        
        for url in urls:
            driverCapitulo.get(url)
            
            if primeira_iteracao:
                sleep(7)
                primeira_iteracao = False
            
            sleep(3)
            
            element_nome_cap = driverCapitulo.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[1]/div[1]/h1/p")
            
            imgs_element = driverCapitulo.find_element(By.XPATH, "/html/body/div/div/div/main/div[6]/div[1]")
            
            soupCapitulo = BeautifulSoup(imgs_element.get_attribute("outerHTML"), "html.parser")
            
            imgs = soupCapitulo.find_all("img")
            
            lista_links_imagens: List[str] = []
            
            # [1:] -> remover primeira imagem (ad do scaner)
            for img in imgs[1:]:
                lista_links_imagens.append(img["src"])
            
            capitulos.append({
                "nomeCapitulo": element_nome_cap.text.split("/ ")[1],
                "paginas": lista_links_imagens,
            })
            
        return capitulos 
    except:
        raise ValueError("Ocorreu um erro, tente novamente.")
    finally:
        driverCapitulo.quit()     


def obterManga(url: str) -> Manga:
    driver = webdriver.Chrome()
    
    try:
        driver.get(url)
        driver.fullscreen_window()
        
        sleep(10)
        
        nome_manga_element = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[3]/div/div[2]/p")
        
        nome_manga = nome_manga_element.text
        
        img_capa = driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[3]/div/div[1]/img[1]").get_attribute("src")
        
        # obter os links dos capítulos
        
        quarta_secao_element = driver.find_element(By.XPATH, "/html/body/div/div/div/main/section[4]/div[1]/span")
        
        numero_secao_capitulos = 4 # caso tenha a section "tags" a seção de capítulos é a 5º
        
        if quarta_secao_element.text == "Tags":
            numero_secao_capitulos = 5
        
        filter_btn = driver.find_element(By.XPATH, f"/html/body/div/div/div/main/section[{numero_secao_capitulos}]/div[1]/div")
        filter_btn.click()
        sleep(1)
        
        button = driver.find_element(By.XPATH, f"/html/body/div/div/div/main/section[{numero_secao_capitulos}]/div[2]/div/div[2]/div/div/div[2]/div")
        button.click()
        sleep(3)
        
        caps_element = driver.find_element(By.XPATH, f"/html/body/div/div/div/main/section[{numero_secao_capitulos}]/div[2]/div/div[2]/div/div/div[1]")
        
        
        caps_soup = BeautifulSoup(caps_element.get_attribute("outerHTML"), "html.parser")
        
        anchors = caps_soup.find_all("a")
        
        driver.quit()
        
        links_capitulos: List[str] = []
        
        for a in anchors:
            if not "grupo" in a["href"]:
                links_capitulos.append(f"https://slimeread.com{a["href"]}")
                
        
        capitulos = obterPaginasCapitulos(links_capitulos)

        manga: Manga = {
            "nomeManga": nome_manga.replace("-", " "),
            "capitulos": capitulos,
            "imgCapa": img_capa,
        }

        return manga
    except:
        raise ValueError("Algo deu errado com o emulador.")
    finally:
        driver.quit()