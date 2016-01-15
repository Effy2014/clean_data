
# coding: utf-8

# In[168]:

import pandas as pd
import numpy as np
import re


# In[169]:

user_info = pd.read_csv('Jan11.csv', header = 0)


# In[170]:

col = user_info.columns.get_loc("Signup Page")


# In[171]:

Ind = user_info[user_info[["Signup Page","Referer"]].isnull().all(axis=1)].index


# In[172]:

Ind[user_info["Coming From"][Ind] == 'JSON']


# In[173]:

###sign up from App
user_info.iloc[Ind[user_info["Coming From"][Ind] == 'JSON'], col] = 'App'


# In[174]:

#filling in missing values in "Signup Page" column
Ind2 = user_info[user_info[["Signup Page","Referer"]].isnull().all(axis=1)].index

user_info.iloc[Ind2,col] = 'New General Student'


# In[175]:

user_info["Signup Page"] = user_info["Signup Page"].fillna('General')


# In[162]:

#user_info["Referer"]=user_info["Referer"].fillna('')


# In[181]:

user_info["types"] = user_info["Signup Page"].map(str) +"/"+user_info["Referer"]


# In[180]:

user_info[user_info["Referer"].isnull()].index


# In[182]:

for i in user_info[user_info["Referer"].isnull()].index:
    user_info["types"][i] = user_info["Signup Page"][i]


# In[184]:

user_info["types"] = [re.sub("//", "/", i) for i in user_info["types"]]


# In[194]:

df = user_info[["ID","types"]]


# In[201]:

out = df.groupby(["types"], sort = True).count().reset_index()


# In[207]:

out.to_csv("out.csv", sep = ",", index = False)


# In[203]:

out.index


# In[ ]:



