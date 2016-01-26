
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[2]:

support = pd.read_csv("GoEnnounce_Export_01-26-2016_01-01-53-PM.csv", header = 0)


# In[5]:

support.columns.values


# In[12]:

support["date"] = support['Date Registered'].map(lambda x : x.split("@")[0])


# In[13]:

support["date"] = pd.to_datetime(support["date"])


# In[28]:

daily = support[["ID", "date"]].groupby(["date"]).count().reset_index()[1010:]


# In[18]:

index = pd.date_range('2015-12-01', periods=31)


# In[20]:

support["Date"]= [d.strftime('%Y-%m-%d') if not pd.isnull(d) else '' for d in support["date"]]
support["This month"] = support["Date"].map(lambda x : x in index) 


# In[21]:

support[support["This month"] == True].shape


# In[24]:

support[(support["date"]<='2015-12-31')&(support["date"]>='2015-12-01')].shape


# In[ ]:



