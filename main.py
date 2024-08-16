from webScrapping import obterCapitulos
from mongo import salvarManga
from time import time

def main():
    url_manga = ""
    while not url_manga:
        print("Somente mangás do mangaonline.biz Exemplo url mangá:")
        print("https://mangaonline.biz/manga/kaiju-no-8/\n")
        
        url_manga = input("URL mangá: ")
        
    capitulos, nome_manga = obterCapitulos(url_manga)
    salvarManga(capitulos, nome_manga)
    
if __name__ == "__main__":
    inicio = time()
    main()
    fim = time()
    print(f"Demorou: ", fim - inicio)