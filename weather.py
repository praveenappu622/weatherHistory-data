#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"E:\project/weatherHistory.csv")


# In[3]:


print(df)


# In[4]:


pd.read_csv(r"E:\project/weatherHistory.csv")


# In[5]:


titles_req = ["Formatted Date", "Apparent Temperature (C)", "Humidity"]
df = df[titles_req]


# In[6]:


df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df = df.set_index('Formatted Date')
df = df.resample('MS').mean()


# In[8]:


df.head()


# In[9]:


plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Tempearture and Humidity with time")
plt.plot(df)


# In[11]:


df_april = df[df.index.month==4]


# In[12]:


plt.figure(figsize=(14,6))
plt.plot(df_april)


# In[ ]:




