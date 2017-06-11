
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import json

file_path = "data/AllSets.json"

with open(file_path) as data_file:  
    data = json.load(data_file)


# In[4]:

i = 0
for key in data:
    print ("key: {}".format(key))
    i += 1
    
print("\nSets: {}".format(i))


# In[5]:

print(data["LEA"]["cards"][0])


# In[6]:

df_lea = pd.DataFrame(data["LEA"]["cards"])

card_info = df_lea[['name', 'manaCost', 'text', 'types', 'toughness', 'power', 'subtypes', 'rarity']]
panel = pd.DataFrame(card_info, index=[0])
print(panel)


# In[7]:

df_lea = pd.DataFrame(data["LEA"]["cards"])

card_info = df_lea[['manaCost', 'types', 'toughness', 'power', 'subtypes', 'rarity']]
panel = pd.DataFrame(card_info)
print(panel)


# In[8]:

df_lea = pd.DataFrame(data["LEA"]["cards"])
df_emn = pd.DataFrame(data["EMN"]["cards"])

card_info_lea = df_lea[['manaCost', 'types', 'toughness', 'power', 'subtypes', 'text']]
card_info_emn = df_emn[['manaCost', 'types', 'toughness', 'power', 'subtypes', 'text']]
panel1 = pd.DataFrame(card_info_lea)
panel2 = pd.DataFrame(card_info_emn)

frames = [panel1, panel2]

print(pd.concat(frames))

