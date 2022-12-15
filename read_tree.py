#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Tree_struct import TreeNode
import json
with open('data_tree_struct.json', 'r') as openfile: 
    # Reading from json file
    json_str = json.load(openfile)
# load the tree
tree = TreeNode.from_dict(json_str)


# In[8]:


parent=tree.getchild(1).getchild(1).getchild(1).getchild(1)


# In[ ]:




