#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# import cubic_zirconia data set


# In[3]:



cubic = pd.read_csv('cubic_zirconia.csv')


# In[4]:


cubic.head()


# In[5]:


# Rows and columns of the data set


# In[6]:


cubic.shape


# In[7]:


cubic.info()


# In[8]:


## columns name

cubic.columns


# In[9]:


## find out NAN value 


# In[10]:


cubic.isna().any()


# In[11]:


## It is true  in the column of depth


# In[12]:


cb = cubic.fillna(0)


# In[13]:


cb.isna().any()


# In[14]:


### statistical description of dataset

cubic.describe()


# In[15]:


cubic.cut.unique()


# In[16]:


cubic.clarity.unique()


# In[ ]:


## visualization


# In[20]:


sns.distplot(cb['depth'])
plt.show()


# In[34]:


sns.distplot(cb['price'],kde=False,color='black')
plt.show()


# In[33]:



sns.jointplot(cb['depth'],cb['price'],kind='hex',color='green')
plt.show()


# In[32]:


sns.pairplot(cb)
plt.show()


# In[ ]:


## finding outliers


# In[35]:


sns.boxplot(cb['depth'])


# In[ ]:




