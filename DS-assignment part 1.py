#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


house = pd.read_excel('DS - Assignment Part 1 data set.xlsx')


# first 5 recordes

# In[3]:


house.head()


# In[45]:


house.info()


# In[4]:


## checking the shape of the data frame


# In[5]:


house.shape


# In[6]:


house.info()


# In[7]:


## checking if there is any null value
house.isnull().any()


# In[8]:


## no null values there


# In[9]:


### so checking for  nan 


# In[10]:


house.isna().any()


# In[11]:


## there is no nan values in the data set


# In[12]:


house.describe()


# In[13]:


## importing libraries


# In[14]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


# heatmap


# In[16]:


plt.figure(figsize=(15,10))
sns.heatmap(house.corr(),annot = True,linewidths=3,cmap='BrBG')


# from the above graph we can see that the realationship between house price and Number of convenience stores, latitude, longitude are in the range of 0.5.They are more correlated than the other feature.Distance from nearest Metro station (km) and price shows a negative relationship (-0.6)

# In[17]:


house['Number of bedrooms'].value_counts().plot(kind='bar')
plt.title('Number of bedrooms',size=20)
plt.xlabel('bedrooms')
plt.ylabel('count')
plt.show()


# As we can see from the visualization 1 bedroom house are sold a little bit more compared to others, but we can see that from the visualization bedrooms numbers doesn't makes any big differents in the sales.

# In[18]:


## Lets see if house size affect the price of house or not


# In[19]:


sns.scatterplot(y = 'House size (sqft)',x = 'House price of unit area',data = house,color ='red',hue='Number of bedrooms')
plt.title('sqft vs price')


# The above visualization show that  the house size from 400 to 600 which has only 1 room and the price of the house resides in 20 to 60,From above 800sft the houses contain 2 and 3 bedroom and also the price of majority of the houses resides in 20 to 60.it seems like house size doesn't influence price greatly, but there are few houses which price is affected by house size

# In[20]:


## next house price and location


# In[21]:


sns.scatterplot(x='longitude',y='House price of unit area',data=house,color='maroon')
plt.title('location vs price')


# This figure tells us about the location of the houses in terms of longitude and it gives us an observation that 121.53 to 121.55 sells houses at much higher amount, and also lot of sales happen in this area

# In[22]:


sns.scatterplot(x='latitude',y='House price of unit area',data=house)


#    Similarly this figure shows price vs latitude and a higher sales occurs from 24.96 to 24.99 at higher price

# In[23]:


sns.scatterplot(x='Number of convenience stores',y='House price of unit area',data = house,color='purple')


# In[24]:


sns.scatterplot(x='Distance from nearest Metro station (km)',y='House price of unit area',data=house,color='gray')


# The above visualization shows us the distance from nearest metro station and price of the houses and it gives us quit an interesting obseravation that majority of houses are sold in the area were distance between metro station is low.

# In[25]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[26]:


l= LinearRegression()


# In[27]:


x=house.drop('House price of unit area',axis=1)
y=house['House price of unit area']


# In[28]:


xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.2,random_state=42)


# In[29]:


l.fit(xtrain,ytrain)


# In[30]:


y_predict = l.predict(xtest)


# In[31]:


print(l.score(xtest,ytest))


# After fitting the data to the model, the prediction is 67% . accuracy of the model is lower than we expected

# In[38]:


x=house.drop('House price of unit area',axis=1)
y=house['House price of unit area']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.2,random_state=42)


# In[39]:


l.fit(xtrain,ytrain)


# In[40]:


ypredict=l.predict(xtest
                  
                  )


# In[41]:


print(l.score(xtest,ytest))


# In[ ]:




