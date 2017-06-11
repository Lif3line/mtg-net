
# coding: utf-8

# In[7]:

import pandas as pd
import numpy as np
import json

file_path = "data/AllSets.json"

with open(file_path) as data_file:  
    data = json.load(data_file)


# In[21]:

i = 0
for key in data:
    print ("key: {}".format(key))
    i += 1
    
print("\nSets: {}".format(i))


# In[24]:

print(data["LEA"]["cards"][0])


# In[32]:

df_lea = pd.DataFrame(data["LEA"]["cards"])

card_info = df_lea[['name', 'manaCost', 'text', 'types', 'toughness', 'power', 'subtypes', 'rarity']]
panel = pd.DataFrame(card_info, index=[0])
print(panel)


# In[38]:

df_lea = pd.DataFrame(data["LEA"]["cards"])

card_info = df_lea[['manaCost', 'types', 'toughness', 'power', 'subtypes', 'rarity']]
panel = pd.DataFrame(card_info)
print(panel)

