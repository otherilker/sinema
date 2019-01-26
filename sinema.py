import requests
from bs4 import BeautifulSoup

url = "https://www.cinemaximum.com.tr/vizyondakiler"

response = requests.get(url)
sayfa_icerigi = response.content

soup = BeautifulSoup(sayfa_icerigi,"html.parser")

puan = input("Puanı giriniz: ")

filmler = soup.find_all("div",{"class":"movie-list-item"})
imdbler = soup.find_all("div",{"class":"movie-rating"})

for filmler, imdbler in zip(filmler,imdbler):
    filmler = filmler.text
    imdbler = imdbler.text

    filmler = filmler.strip()
    filmler = filmler.replace("\n","")

    imdbler = imdbler.strip()
    imdbler = imdbler.replace("\n", "")

    filmler = filmler.replace("Bilet Al", "")
    imdbler = imdbler.replace("Bilet Al", "")

    print(filmler)
    print(imdbler)

    if (float(puan) > 9):
        print("Film Adı: {} İmdb Puanı: {}".format(filmler,imdbler))
























