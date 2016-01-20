
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[8]:

user = pd.read_csv('GoEnnounce_Export_01-18-2016_11-01-36-AM.csv', header = 0)
mission = pd.read_csv('GoEnnounce_Mission_Export_01-18-2016_03-01-02-PM.csv', header = 0)


# In[9]:

info = user[["ID", "Date Registered", "Referer", "Signup Page", "Coming From"]]


# In[10]:

combind = mission.merge(info, how = 'left', left_on = ' User ID', right_on = 'ID')


# In[11]:

combind[" Start Date"] = pd.to_datetime(combind[" Start Date"])
combind["Date Registered"] = pd.to_datetime(combind["Date Registered"])


# In[13]:

combind["Date Registered"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in combind["Date Registered"]]
combind["Start Date"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in combind[" Start Date"]]


# In[79]:


#index4 = pd.date_range('2016-01-04', periods=7)
index4 = pd.date_range('2016-01-11', periods=7)


# In[80]:

index4


# In[81]:

#index = [pd.date_range('2015-12-07', periods=7), pd.date_range('2015-12-14', periods=7), pd.date_range('2015-12-21', periods=7),
#        pd.date_range('2015-12-28', periods=7), pd.date_range('2016-01-04', periods=7), pd.date_range('2016-01-11', periods=7)]


# In[82]:

#combind["week"] = 0
#combind["Mission"] = 0


# In[83]:

combind["Register4"] = combind["Date Registered"].map(lambda x : x in index4)
combind["Mission4"] = combind["Start Date"].map(lambda x : x in index4)


# In[84]:

#combind["Register2"] = combind["Date Registered"].map(lambda x : x in index2)
#combind["Mission2"] = combind["Start Date"].map(lambda x : x in index2)


# In[85]:

sum(combind["Mission4"])


# In[86]:

df1 = combind[combind["Mission4"] == True]


# In[87]:

df1 = df1.reset_index()
col = df1.columns.get_loc("Signup Page")
Ind = df1[df1[["Signup Page","Referer"]].isnull().all(axis=1)].index
df1.iloc[Ind[df1["Coming From"][Ind] == 'JSON'], col] = 'App'
Ind2 = df1[df1[["Signup Page","Referer"]].isnull().all(axis=1)].index
df1.iloc[Ind2,col] = 'New General Student'
df1["Signup Page"] = df1["Signup Page"].fillna('General')
df1["Referer"]=df1["Referer"].fillna('')
df1["types"] = df1["Signup Page"].map(str) +"/"+df1["Referer"]


# In[88]:

to_do = df1[["Register4","types", "ID"]]


# In[89]:

to_do.groupby(["types","Register4"]).count().reset_index()


# In[ ]:



