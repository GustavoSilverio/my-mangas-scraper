from webScrapping import obterCapitulos
from mongo import salvarCapitulos

def main():
    nome_manga = ""
    while not nome_manga:
        print("Somente mangás do mangaonline.biz Exemplo url mangá:")
        print("https://mangaonline.biz/manga/kaiju-no-8/\n")
        nome_manga = input("URL mangá: ")
        
    capitulos, nome_manga = obterCapitulos(nome_manga)
    salvarCapitulos(capitulos, nome_manga)
    
if __name__ == "__main__":
    main()