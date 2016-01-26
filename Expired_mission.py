
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[189]:

mission = pd.read_csv('GoEnnounce_Mission_Export_01-25-2016_03-01-51-PM.csv', header = 0, skip_blank_lines=True)


# In[190]:

mission[" End Date"] = pd.to_datetime(mission[" End Date"])


# In[191]:

mission["Raised"] = (mission[" Amount Raised to Date"].replace( '[\$,)]','', regex=True )
                                                                      .replace( '[(]','-',   regex=True ).astype(int))


# In[192]:

expiring = pd.date_range('2016-01-26', periods=7)
expired = pd.date_range('2016-01-19', periods = 7)


# In[193]:

mission["expiring"] = mission[" End Date"].map(lambda x : x in expiring)
mission["expired"] = mission[" End Date"].map(lambda x : x in expired)
mission = mission.fillna('')


# In[194]:

has_donation = mission[(mission["expiring"] == True)&(mission["Raised"]>0)]
mission = mission[~mission.isin(has_donation).all(1)]
has_visit = mission[(mission["expiring"] == True)&(mission[" Total Visits"]>20)]
mission = mission[~mission.isin(has_visit).all(1)]
expiring_others = mission[mission["expiring"] == True]
had_donation = mission[(mission["expired"] == True)&(mission["Raised"]>0)]
mission = mission[~mission.isin(had_donation).all(1)]
had_visit = mission[(mission["expired"] == True)&(mission[" Total Visits"]>20)]
mission = mission[~mission.isin(had_visit).all(1)]
expired_others = mission[mission["expired"] == True]


# In[198]:

has_donation = has_donation.drop(["Raised", "expiring", "expired"], 1).reset_index()
has_visit = has_visit.drop(["Raised", "expiring", "expired"], 1).reset_index()
expiring_others = expiring_others.drop(["Raised", "expiring", "expired"], 1).reset_index()
had_donation = had_donation.drop(["Raised", "expiring", "expired"], 1).reset_index()
had_visit = had_visit.drop(["Raised", "expiring", "expired"], 1).reset_index()
expired_others = expired_others.drop(["Raised", "expiring", "expired"], 1).reset_index()


# In[200]:

import csv
with open('results.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['less than 7 days remaining-has donation'])
    csvwriter.writerow(has_donation.columns.values)
    for i in range(has_donation.shape[0]):
         csvwriter.writerow(has_donation.loc[i,])
    csvwriter.writerow(['less than 7 days remaining-has >20 visits'])
    csvwriter.writerow(has_visit.columns.values)
    for i in range(has_visit.shape[0]):
         csvwriter.writerow(has_visit.loc[i,])
    csvwriter.writerow(['rest in remaining mission'])
    csvwriter.writerow(expiring_others.columns.values)
    for i in range(expiring_others.shape[0]):
         csvwriter.writerow(expiring_others.loc[i,])
    csvwriter.writerow(['0 days remaining - has donation'])
    csvwriter.writerow(had_donation.columns.values)
    for i in range(had_donation.shape[0]):
         csvwriter.writerow(had_donation.loc[i,])
    csvwriter.writerow(['0 days remaining - has >20 visits'])
    csvwriter.writerow(had_visit.columns.values)
    for i in range(had_visit.shape[0]):
         csvwriter.writerow(had_visit.loc[i,])
    csvwriter.writerow(['rest in expired mission'])
    csvwriter.writerow(expired_others.columns.values)
    for i in range(expired_others.shape[0]):
         csvwriter.writerow(expired_others.loc[i,])


# In[71]:

pieces = {'less than 7 days remaining-has donation': has_donation, 
          'less than 7 days remaining-has >20 visits': has_visit,
          'rest in remaining mission' : expiring_others,
          '0 days remaining - has donation': had_donation,
          '0 days remaining - has >20 visits' : had_visit,
          'rest in expired mission' : expired_others,}

result = pd.concat(pieces)


# In[72]:

result.to_csv("results.csv")


# In[ ]:



