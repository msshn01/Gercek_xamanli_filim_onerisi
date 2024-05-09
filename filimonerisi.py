from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import json


def dataUpload():
    url = "https://www.sinemalar.com/filmler/en-iyi-filmler"
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    istek = requests.get(url,headers).text
    soup = BeautifulSoup(istek , "html.parser")
    liste=soup.find("div",attrs={"id":"sinepediResults"}).find_all("a",attrs={"class":"movie"})

    #result tüm zamanlarin en iyi filimleri
    df_movie_best=[]
    for filim in liste:
        movieName=filim.find("div",attrs={"class":"name"}).text
        moviegenre=filim.find("div",attrs={"class":"genre"}).find("span").text
        moviegenre=moviegenre.replace(" ","")
        moviegenre.split(",")
        df_movie_best.append({"name":movieName,"genre":moviegenre})
        data=pd.DataFrame(df_movie_best)
    #result=data.groupby('genre').get_group("Dram")

    url2="https://www.sinemalar.com/filmler/pekyakinda"
    istek2=requests.get(url2,headers).text

    soup2=BeautifulSoup(istek2,"html.parser")
    liste2=soup2.find("div",{"class":"movies"}).find_all("a",attrs={"class":"movie"})
    df_movie_new=[]
    for i in liste2:
        movieName2=i.find("div",attrs={"class":"name"}).text
        moviegenre2=i.find("div",attrs={"class":"genre"}).text
        moviegenre2=moviegenre2.replace(" ","")
        moviegenre.split(",")
        df_movie_new.append({"name":movieName2,"genre":moviegenre2})
        data2=pd.DataFrame(df_movie_new)
    """
    data şimdiye kadarki en iyi filimler selenium ile artirilicak
    data2 ise yakinda cikacak olan filimler
    """
    return [data,data2]    









class Movie:
    def __init__(self):
        self.dataName=""

    def datasection(self,seçim):
        self.dataName=dataUpload()[int(seçim)-1]

    def dowloads(self,tür):
        result=self.dataName[self.dataName["genre"]==f"{tür}"]
        if tür =="x":
            result = self.dataName
        return result




movie=Movie()







while True:
    print("Filim öneriye hoşgeldiniz")
    print("1)En çok sevilen filimler \n2)Yakında vizyona girecekler\n3)Çikiş")
    seçim=input("SEÇİMİNİZ= ==> ")
    if seçim =="3":
        break
    else:
        if seçim =="1":
            movie.datasection("1")
            tür=input("Aranan filim türü nedir(Dram,Aksiyon,Gerilim,Macera,Fantastik,Suç)(yoksa entere basın): ")
            if tür !="":
                print(movie.dowloads(tür))
            else:
                print(print(movie.dowloads("x")))
        elif seçim=="2":
            movie.datasection("2")
            tür=input("Aranan filim türü nedir(Dram,Aksiyon,Gerilim,Macera,Fantastik,Suç,Komedi)(yoksa entere basın): ")
            if tür !="":
                print(movie.dowloads("x"))
            else:
                print(print(movie.dowloads("x")))

