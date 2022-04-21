#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from datetime import datetime


# In[51]:


def changeDate(date_time_str):
    r = date_time_str
    if date_time_str.find("/") != -1:
        day,month,year = date_time_str.split("/")
        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month
        date_time_str = day + "/" + month + "/" + year
        date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y')
        r = date_time_obj.strftime("%A %d %b %Y")
    return(r)


# In[2]:


data_url ="https://docs.google.com/spreadsheets/d/e/2PACX-1vT-1hbZ9phjvuPZ69h-dVa6gYtGjvAUr1QFxCgmx9CSvug49eFgHzOwLvQBQEJdbSYREmU1UlNOQHoq/pub?gid=137863374&single=true&output=csv"


# In[3]:


seminars = pd.read_csv(data_url)


# In[54]:


seminars.date = seminars.date.apply(changeDate)


# In[56]:


del seminars['Timestamp']


# In[59]:


seminars.to_csv("../docs/_data/seminars.csv", index=False)

