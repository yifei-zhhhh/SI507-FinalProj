#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from Tree_struct import TreeNode
import numpy as np


# In[2]:


data=pd.read_csv("raw_movie_info.csv")
idx=np.linspace(0,249,250).astype(int)
tree=TreeNode(idx.tolist())


# In[3]:


# first question "Do you want this movie to be more than 125 minutes (including 125)"
yes_1=[]
no_1=[]
for i in idx:
    if int(data["Runtime"][i].split(" ")[0])>=125:
        yes_1.append(int(i))
    else:
        no_1.append(int(i))
tree.children.append(TreeNode(yes_1))
tree.children.append(TreeNode(no_1))


# In[4]:


# Second Question: Do you want a movie that is younger than 1995 (include 1995)?
def q2(node,temp):
    if node.howmanychild()==0:
        yes=[]
        no=[]
        for i in node.name:
            try:
                if int(data["Year"][i])>=1995:
                    yes.append(int(i))
                else:
                    no.append(int(i))
            except:
                no.append(int(i))
        node.children.append(TreeNode(yes))
        node.children.append(TreeNode(no))
        return temp
    else:
        return temp+q2(node.getchild(0),0)+q2(node.getchild(1),0)
tmp=q2(tree,0)


# In[5]:


# Third question: Do you require a English version of the movie?

def q3(node,temp):
    if node.howmanychild()==0:
        yes=[]
        no=[]
        for i in node.name:
            no.append(int(i))
            try:
                if "English" in data.iloc[i]["Language"]:
                    yes.append(int(i))
            except:
                continue
        node.children.append(TreeNode(yes))
        node.children.append(TreeNode(no))
        return temp
    else:
        return temp+q3(node.getchild(0),0)+q3(node.getchild(1),0)
tmp=q3(tree,0)


# In[6]:


# fourth question "Do you want this movie to have a rotten tomato rating that above average"
# get the average score
rotten=[]

for i in idx:
    try:
        rotten.append(int(data["Rotten Tomatoes"][i][:-1]))
    except:
        continue

average_rotten=np.mean(rotten)
# Classify according to the question 4
def q4(node,temp):
    if node.howmanychild()==0:
        yes=[]
        no=[]       
        for i in node.name:
            no.append(int(i))
            try:
                if(int(data["Rotten Tomatoes"][i][:-1])>=average_rotten):
                    yes.append(int(i))
            except:
                continue
        node.children.append(TreeNode(yes))
        node.children.append(TreeNode(no))
        return temp
    else:
        return temp+q4(node.getchild(0),0)+q4(node.getchild(1),0)
tmp=q4(tree,0)


# In[7]:


#fifth question "Do you want only want movies that are nominated or won Oscars?"
def q5(node,temp):
    if node.howmanychild()==0:
        yes=[]
        no=[]
        for i in node.name:
            no.append(int(i))
            try:
                if "Oscar" in data.iloc[i]["Awards"]:
                    yes.append(int(i))
            except:
                continue
        node.children.append(TreeNode(yes))
        node.children.append(TreeNode(no))
        return temp
    else:
        return temp+q5(node.getchild(0),0)+q5(node.getchild(1),0)
tmp=q5(tree,0)


# In[8]:


import json
json_str = json.dumps(tree, indent=2)
with open("data_tree_struct.json", "w") as outfile:
    outfile.write(json_str)

