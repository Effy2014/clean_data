
# coding: utf-8

# In[94]:

import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[95]:

user_info = pd.read_csv('GoEnnounce_Export_01-13-2016_08-01-47-AM.csv', header = 0, skip_blank_lines=True)


# In[96]:

user_info["Date Registered"] = pd.to_datetime(user_info["Date Registered"])
#user_info["Day"] = user_info["Date Registered"].dt.day
#user_info["Month"] = user_info["Date Registered"].map(lambda x: x.strftime('%b')) 


# In[97]:

user_info["Daily"] = user_info["Date Registered"].map(lambda x: x.strftime('%b-%d-%y'))


# In[98]:

#user_info["Day"] = map(str, user_info["Day"])


# In[99]:

#user_info["Daily"] = user_info["Day"].map(str) + "-" + user_info["Month"]


# In[100]:

col = user_info.columns.get_loc("Signup Page")


# In[101]:

Ind = user_info[user_info[["Signup Page","Referer"]].isnull().all(axis=1)].index


# In[102]:

#Ind[user_info["Coming From"][Ind] == 'JSON']


# In[103]:

###sign up from App
user_info.iloc[Ind[user_info["Coming From"][Ind] == 'JSON'], col] = 'App'


# In[104]:

#filling in missing values in "Signup Page" column
Ind2 = user_info[user_info[["Signup Page","Referer"]].isnull().all(axis=1)].index
user_info.iloc[Ind2,col] = 'New General Student'


# In[105]:

user_info["Signup Page"] = user_info["Signup Page"].fillna('General')


# In[106]:

user_info["Referer"]=user_info["Referer"].fillna('')


# In[107]:

user_info["types"] = user_info["Signup Page"].map(str) +"/"+user_info["Referer"]


# In[108]:

user_info["types"] = [re.sub("//", "/", i) for i in user_info["types"]]


# In[109]:

user_info["types"] = user_info["types"].str.lower()


# In[110]:

df = user_info[["ID","Daily","types"]]


# In[111]:

df[df["Daily"] == "Dec-20"].to_csv('Dec-20.csv')


# In[112]:

out = df.groupby(["Daily","types"], sort = True).count().reset_index()


# In[113]:

out_put = out.pivot(index='types', columns='Daily', values='ID')


# In[114]:

out_put = out_put.fillna('')


# In[121]:

out_put.to_csv("out_put.csv", sep = ",")


# In[116]:

#out.columns = ['Existing Student Accounts', '12-Jan']


# In[117]:

#out.to_csv("out.csv", sep = ",", index = False)


# In[178]:

master = pd.read_csv("Master_Daily.csv", index_col = 0)


# In[131]:

#result = pd.merge(master, out, on = 'Existing Student Accounts', how = 'outer', sort = False)


# In[132]:

#result.to_csv("Master_Daily.csv", index = False)


# In[182]:

add = out_put[["Dec-23-15", "Dec-24-15", "Dec-25-15", "Dec-26-15","Dec-27-15","Dec-28-15","Dec-29-15","Dec-30-15","Dec-31-15", "Jan-01-16","Jan-02-16","Jan-03-16", "Jan-04-16", "Jan-05-16","Jan-06-16", "Jan-07-16","Jan-08-16","Jan-09-16","Jan-10-16","Jan-11-16", "Jan-12-16", "Jan-13-16"]]


# In[180]:

master.index = master.index.str.lower()


# In[183]:

add.index = add.index.map(lambda x : x[:-1] if x[-1] == '/' else x)


# In[194]:

result = pd.merge(master, add, left_index=True, right_index=True, how = 'outer')


# In[196]:

result.to_csv("result.csv")


# In[ ]:



