
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[63]:

user = pd.read_csv('GoEnnounce_Export_01-18-2016_11-01-36-AM.csv', header = 0)
mission = pd.read_csv('GoEnnounce_Mission_Export_01-18-2016_03-01-02-PM.csv', header = 0)


# In[111]:

info = user[["ID", "Date Registered", "Referer", "Signup Page", "Coming From"]]


# In[112]:

combind = mission.merge(info, how = 'left', left_on = ' User ID', right_on = 'ID')


# In[113]:

combind[" Start Date"] = pd.to_datetime(combind[" Start Date"])
combind["Date Registered"] = pd.to_datetime(combind["Date Registered"])


# In[114]:

combind["Date Registered"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in combind["Date Registered"]]
combind["Start Date"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in combind[" Start Date"]]


# In[115]:

combind["New"] = combind["Start Date"] == combind["Date Registered"]


# In[116]:

df1 = combind[combind["Start Date"] > "2015-12-01"]


# In[124]:

df1 = df1.reset_index()


# In[125]:

col = df1.columns.get_loc("Signup Page")


# In[126]:

Ind = df1[df1[["Signup Page","Referer"]].isnull().all(axis=1)].index


# In[128]:

df1.iloc[Ind[df1["Coming From"][Ind] == 'JSON'], col] = 'App'


# In[129]:

Ind2 = df1[df1[["Signup Page","Referer"]].isnull().all(axis=1)].index
df1.iloc[Ind2,col] = 'New General Student'


# In[130]:

df1["Signup Page"] = df1["Signup Page"].fillna('General')
df1["Referer"]=df1["Referer"].fillna('')


# In[131]:

df1["types"] = df1["Signup Page"].map(str) +"/"+df1["Referer"]


# In[133]:

df2 = df1[[" User ID","Start Date", "New", "types"]]


# In[135]:

df3 = df2.groupby(["Start Date", "types", "New"],sort = True).count().reset_index()


# In[141]:

df_new = df3[df3["New"] == True]


# In[149]:

df_existing = df3[df3["New"] == False]


# In[150]:

out = df_existing.pivot(index = "types", columns = "Start Date", values = " User ID")


# In[153]:

out.to_csv("out_put3.csv", sep = ",")


# In[77]:

df = combind[["ID","Start Date","New"]]


# In[80]:

to_do = df[df["Start Date"] > "2015-12-01"]


# In[154]:

total = to_do.groupby(["Start Date", "New"], sort = True).count().reset_index()


# In[ ]:



