#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis Project
# 

# #  Step 1-Importing Libaries

# In[ ]:


pandas is used for data manipulation and analysis
numpy is used for numerical operations.
matplotlib.pyplot and seaborn are used for data visualization.


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Step 2- Create the data frame

# In[9]:


dataframe =  pd.read_csv("C:\\Users\\ARSH BHARDWAJ\\Downloads\\Zomato data  (1).csv")
dataframe


# # Covert the data type  of column-rate

# In[10]:


#remove after ''/' part denominator
def handleRate(value):
    value = str(value).split('/')
    value=value[0];
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[11]:


#summary of data
dataframe.info()


# # Type of Restaurant and majority of restaurants fall in which type

# In[12]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# # count votes for each restaurant

# In[13]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)


# # Majority of restaurants received ratingd

# In[14]:


dataframe.head()


# In[15]:


plt.hist(dataframe['rate'],bins=5)
plt.title("Ratings Distribution")
plt.show()


# # Average money spend by couples

# In[16]:


sns.countplot(x=dataframe['approx_cost(for two people)'])
plt.xlabel("approx_cost(for two people)")


# # Which mode receives maximum rating offline or online

# In[17]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y= 'rate', data = dataframe)


# # Which type of restaurant recieved more offline orders

# In[19]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True,cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed in (Type)")
plt.show()


# In[ ]:




