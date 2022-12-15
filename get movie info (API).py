
import requests
import pandas as pd


movie_list=pd.read_csv("movie_list.csv")
title=movie_list["name"]
year=movie_list["year"].astype(str)


imdb=[]
tomato=[]
metacritic=[]
i=0
movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&t='+title[i]+'&y='+year[i]).json()
imdb.append(pd.DataFrame(movieInfo)["Ratings"][0].get('Value'))
tomato.append(pd.DataFrame(movieInfo)["Ratings"][1].get('Value'))
metacritic.append(pd.DataFrame(movieInfo)["Ratings"][2].get('Value'))
movie_detail=pd.DataFrame(movieInfo).loc[[0], :]

for i in range(1,250):
    movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&t='+title[i]+'&y='+year[i]).json()
    try:
        imdb.append(pd.DataFrame(movieInfo)["Ratings"][0].get('Value'))
    except:
        imdb.append("N/A")
    try:
        tomato.append(pd.DataFrame(movieInfo)["Ratings"][1].get('Value'))
    except:
        tomato.append("N/A")
    try:
        metacritic.append(pd.DataFrame(movieInfo)["Ratings"][2].get('Value'))
    except:
        metacritic.append("N/A")
    temp=pd.DataFrame(movieInfo).loc[[0], :]
    movie_detail=pd.concat([movie_detail, temp], ignore_index=True)



metacritic[226]=tomato[226]
tomato[226]="N/A"
metacritic[195]=tomato[195]
tomato[195]="N/A"
tomato[234]="N/A"



movie_detail["IMDB"]=pd.DataFrame(imdb)
movie_detail["Rotten Tomatoes"]=pd.DataFrame(tomato)
movie_detail["Metacritic"]=pd.DataFrame(metacritic)



movie_detail.to_csv("raw_movie_info.csv",index=False)






