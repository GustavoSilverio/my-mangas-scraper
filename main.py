from webScrapping import fazerWebScrapping, sites
from mongo import salvarManga
from time import time

def main():
    print("Somente os mangas dos seguintes sites são aceitos:\n")

    for dominio in sites.keys():
        print(f"- {dominio}")
    
    url_manga = input("\nURL mangá: ")
    manga = fazerWebScrapping(url_manga)
    
    salvarManga(manga)

    
if __name__ == "__main__":
    inicio = time()
    main()
    fim = time()
    print(f"Elapsed time: {fim - inicio:.2f} seconds")