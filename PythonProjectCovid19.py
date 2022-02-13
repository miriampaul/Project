#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[15]:


data=pd.read_csv(r'C:\Users\miria\OneDrive\GoogleDataAnalytics\Project\covid19_italy_province.csv')


# In[16]:


data.head()


# In[17]:


data.columns


# In[13]:


data1=pd.read_csv(r'C:\Users\miria\OneDrive\GoogleDataAnalytics\Project\covid19_italy_region.csv')


# In[14]:


data1.head()


# In[18]:


data1.columns


# In[19]:


data1.tail()


# In[20]:


data.describe()


# In[21]:


data.IsNull()


# In[22]:


data1.isnull()


# In[23]:


data1.isnull().sum()


# # relating the variables with scatterplots

# In[26]:


data1.describe()


# In[28]:


# dsd
data1.columns


# In[30]:


sns.relplot(x='TotalPositiveCases',y='Recovered', data=data1)


# In[33]:


sns.relplot(x='TotalPositiveCases',y='Deaths',data=data1)


# In[34]:


sns.relplot(x='TotalPositiveCases',y='CurrentPositiveCases',data=data1)


# In[35]:


sns.relplot(x='TotalPositiveCases',y='TotalHospitalizedPatients',data=data1)


# In[38]:


sns.relplot(x='TotalPositiveCases',y='TestsPerformed',hue='Recovered',data=data1)


# In[37]:


sns.pairplot(data1)


# In[41]:


sns.relplot(x='HomeConfinement',y='TotalPositiveCases',kind='line',data=data1)


# In[42]:


sns.relplot(x='TotalPositiveCases',y='HomeConfinement',kind='line',data=data1)


# In[44]:


data1.columns


# In[ ]:


sns.catplot(x='Recovered',y='TotalPositiveCases',data=data1)


# In[ ]:


#Conclusion- Work needs to ne done on reducing total hospitalized patients. 
#Number of deaths to be reduced .


# In[ ]:




