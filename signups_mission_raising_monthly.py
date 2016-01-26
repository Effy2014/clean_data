
# coding: utf-8

# In[69]:

import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[70]:

user = pd.read_csv('GoEnnounce_Export_01-21-2016_10-01-47-AM.csv', header = 0)
mission = pd.read_csv('GoEnnounce_Mission_Export_01-21-2016_05-01-35-PM.csv', header = 0)


# In[71]:

user["Date Registered"] = pd.to_datetime(user["Date Registered"])
user["year"] = user["Date Registered"].dt.year
user["month"] = user["Date Registered"].dt.month
user["day"] = user["Date Registered"].dt.day


# In[72]:

#daily_new_user  = user[(user["year"] == 2015)&(user["month"] == 12)&(user["day"] == 23)].reset_index()
#daily_new_user.shape


# In[73]:

monthly_new_user  = user[(user["year"] == 2015)&(user["month"] == 12)].reset_index()
monthly_new_user.shape


# In[74]:

#getting monthly newly sign up users
col = monthly_new_user.columns.get_loc("Signup Page")
Ind = monthly_new_user[monthly_new_user[["Signup Page","Referer"]].isnull().all(axis=1)].index
monthly_new_user.iloc[Ind[monthly_new_user["Coming From"][Ind] == 'JSON'], col] = 'App'
Ind2 = monthly_new_user[monthly_new_user[["Signup Page","Referer"]].isnull().all(axis=1)].index
monthly_new_user.iloc[Ind2,col] = 'New General Student'
monthly_new_user["Signup Page"] = monthly_new_user["Signup Page"].fillna('General')
monthly_new_user["Referer"]=monthly_new_user["Referer"].fillna('')
monthly_new_user["types"] = monthly_new_user["Signup Page"].map(str) +"/"+monthly_new_user["Referer"]


# In[75]:

out1 = monthly_new_user[["types", "ID"]].groupby(["types"]).count().reset_index()


# In[98]:

index4 = pd.date_range('2015-12-01', periods=31)


# In[99]:

#preparing data
info = user[["ID", "Date Registered", "Referer", "Signup Page", "Coming From"]]
combind = mission.merge(info, how = 'left', left_on = ' User ID', right_on = 'ID')
combind[" Start Date"] = pd.to_datetime(combind[" Start Date"])
combind["Date Registered"] = pd.to_datetime(combind["Date Registered"])
combind["Date Registered"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in combind["Date Registered"]]
combind["Start Date"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in combind[" Start Date"]]


# In[100]:

#getting data 
combind["Register4"] = combind["Date Registered"].map(lambda x : x in index4)
combind["Mission4"] = combind["Start Date"].map(lambda x : x in index4)


# In[101]:

#getting new users 
new_user = combind[combind["Mission4"] == True].reset_index()
col = new_user.columns.get_loc("Signup Page")
Ind = new_user[new_user[["Signup Page","Referer"]].isnull().all(axis=1)].index
new_user.iloc[Ind[new_user["Coming From"][Ind] == 'JSON'], col] = 'App'
Ind2 = new_user[new_user[["Signup Page","Referer"]].isnull().all(axis=1)].index
new_user.iloc[Ind2,col] = 'New General Student'
new_user["Signup Page"] = new_user["Signup Page"].fillna('General')
new_user["Referer"]=new_user["Referer"].fillna('')
new_user["types"] = new_user["Signup Page"].map(str) +"/"+new_user["Referer"]


# In[105]:

out2 = new_user[["Register4","types", "ID"]].groupby(["Register4","types"],sort=True).count().reset_index()


# In[107]:

out2

