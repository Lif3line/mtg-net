
# coding: utf-8

# In[7]:

import pandas as pd
import numpy as np
import json

file_path = "data/AllSets.json"

with open(file_path) as data_file:  
    data = json.load(data_file)
    
df=pd.DataFrame(data)


# In[21]:

i = 0
for key in data:
    print ("key: {}".format(key))
    i += 1
    
print("\nSets: {}".format(i))


# In[16]:

print(data["LEA"]["cards"])


# In[11]:

all_cards = pd.DataFrame(df, index=["cards"])
pd.DataFrame(all_cards, index=["name"])

