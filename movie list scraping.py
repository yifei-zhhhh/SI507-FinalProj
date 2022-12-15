
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import json




url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")



movies=soup.find_all("td", class_="titleColumn")



name=[]
year=[]
for i in range(0,250):
    movie_full=movies[i].text[13:].replace("\n"," ").strip()
    movie_year=movie_full[-5:-1]
    movie_name=movie_full[:-6].strip()
    name.append(movie_name)
    year.append(movie_year)



movie_list=pd.DataFrame(name)
movie_list["year"]=pd.DataFrame(year)
movie_list.columns=["name","year"]


movie_list.to_csv("movie_list.csv",index=False)





