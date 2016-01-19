
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from datetime import datetime


# In[3]:

user_info = pd.read_csv('GoEnnounce_Export_01-18-2016_11-01-36-AM.csv', header = 0)


# In[5]:

user_info["Date Registered"] = pd.to_datetime(user_info["Date Registered"])


# In[9]:

track = user_info[user_info["Date Registered"]<"2016-01-18"]


# In[13]:

track[["Referral Count", "Share Count", "Badge Count"]].sum(axis = 0)


# In[ ]:



