#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
from Tree_struct import TreeNode
import numpy as np
import json
import webbrowser
# install tabulate


# In[2]:


with open('data_tree_struct.json', 'r') as openfile: 
    # Reading from json file
    json_str = json.load(openfile)
# load the tree
tree = TreeNode.from_dict(json_str)


# In[3]:


data=pd.read_csv("raw_movie_info.csv")


# In[4]:


print("---------------------------------------\n\n")
print("Welcome to movie recommendation system!\n\n")
print("---------------------------------------")
print("For the questions below, please answer yes or no: \n")


# In[5]:


# Simulate some of the user input
y=["yes","y","Y","Yes","Yeah","yeah"]
n=["no","n","N","No"]

def valid(ans):
    if ans in y:
        return 1
    elif ans in n:
        return 2
    else: 
        return 0
def vnum(ans,ln):
    if ans.isdigit():
        if int(ans)<=ln and int(ans)>=1:
            return 1
        else:
            return 2
    elif ans in n:
        return 3
    else:
        return 0


# In[6]:


# ask user input for the questions
q1=input("Do you want this movie to be more than 125 minutes (including 125)?\n")
while(valid(q1)==0):
    q1=input("Please give a valid answer, choose from yes or no:\n")
    
q2=input("Do you want a movie that is younger than 1995 (include 1995)?\n")
while(valid(q2)==0):
    q2=input("Please give a valid answer, choose from yes or no:\n")
    
q3=input("Do you require a English version of the movie?\n")
while(valid(q3)==0):
    q3=input("Please give a valid answer, choose from yes or no:\n")
    
q4=input("Do you want this movie to have a rotten tomato rating that above average?\n")
while(valid(q4)==0):
    q4=input("Please give a valid answer, choose from yes or no:\n")
    
q5=input("Do you want only want movies that are nominated or won Oscars?\n")
while(valid(q5)==0):
    q5=input("Please give a valid answer, choose from yes or no:\n")


# In[7]:


# Get the answer from the tree
options=[valid(q1)-1,valid(q2)-1,valid(q3)-1,valid(q4)-1,valid(q5)-1]
s1=tree.getchild(options[0])
s2=s1.getchild(options[1])
s3=s2.getchild(options[2])
s4=s3.getchild(options[3])
s5=s4.getchild(options[4])


# In[14]:


def print_result(s5,i):
    d=data.iloc[s5.name[i-1]]
    title=d["Title"]
    url=d["Poster"]
    d=pd.DataFrame(d[["Year","Runtime","Genre","Director","Writer","Actors","Language","IMDB","Rotten Tomatoes","Metacritic"]])
    d.columns=[title]
    print(d.to_markdown())
    return url


# In[20]:


# Display output
print("\nWell Done! Let's see what's recommended to you!\n")
if(len(data.Title[s5.name].values)>=10):
    for i in range(0,10):
        ln=10
        print(str(i+1)+"   " +data.Title[s5.name].values[i])
else:
    i=1
    for name in data.Title[s5.name].values:
        ln=len(data.Title[s5.name].values)
        print(str(i)+"   "+name)
q=input("\n Do you want to know more about a movie? If yes, please enter the number of the movie. If no, please enter no:\n")

while(vnum(q,ln)==0 or vnum(q,ln)==2):
    if vnum(q,ln)==0:
        q=input("\n Please give a valid input!\n")
    else:
        q=input(f"\n Please enter something in 1 to {ln}\n")

res_q=vnum(q,ln)
if(res_q==1):
    url=print_result(s5,int(q))
    newq=input("\nDo you want to see the poster of the movie?\n")
    while(valid(newq)==0):
        newq=input("Please give a valid answer, choose from yes or no:\n")
    if(valid(newq)==1):
        print(f"\nLaunching\n{url}\nin web browser...")
        webbrowser.open(url,new=2,autoraise=True)
print("\n---------------------------------------\n\n")
print("         Thank you for using!         \n\n")
print("---------------------------------------")
    


# In[ ]:




