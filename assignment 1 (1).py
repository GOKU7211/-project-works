#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd 
import numpy as np
##Read the data set


# In[2]:


game = pd.read_csv('Laliga.csv')


# In[3]:


game.head()


# In[4]:


game


# In[ ]:


##  Replace dashes with 0 to make sure you can perform arithmetic operations on the data.


# In[7]:


game.replace('-',0,inplace=True)


# In[18]:


game


# In[13]:


## Print the list of teams which came Top 5 in terms of points 


# In[17]:


game[game['Points']>=3368]['Team']


# In[ ]:


## Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences.


# In[42]:


game["Goal_diff_count"] = game['GoalsFor'] - game['GoalsAgainst']


# In[43]:


game['Goal_diff_count']


# In[ ]:


## Using the same function, find the team which has maximum and minimum goal difference. 


# In[44]:


game[game['Goal_diff_count']==game['Goal_diff_count'].min()]


# In[45]:


game[game['Goal_diff_count']==game['Goal_diff_count'].max()]


# In[ ]:


## Create a new column with name “Winning Percent” and append it to the data set
## If there are any numerical error, replace it with 0%


# In[51]:


game["WinningPrecent"] = (game['GamesWon']/game['GamesPlayed'])*100


# In[62]:


game["WinningPrecent"].replace('NaN',np.nan)


# In[63]:


game["WinningPrecent"].fillna(0)


# In[64]:


## Print the top 5 teams which has the highest Winning percentage


# In[65]:


game[game["WinningPrecent"]>=43]['Team']


# In[71]:


## Group teams based on their “Best position” and print the sum of their points for all positions


# In[70]:


game.groupby('BestPosition').sum()['Points']


# In[ ]:




