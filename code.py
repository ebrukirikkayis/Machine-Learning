#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

#from subprocess import check_output
#print(check_output(["ls", "../ml"]).decode("utf8"))

import os
for dirname, _, filenames in os.walk("C:\\Users\EBRU\Desktop\ml"):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[13]:


data= pd.read_csv('C:\\Users\EBRU\Desktop\ml\pokemon.csv')
data.head()


# In[14]:


data.info()


# In[15]:


data.corr()


# In[16]:


#correlation map
f,ax=plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.show()


# In[17]:


data.head(10)


# In[18]:


data.columns


# In[31]:


#line Plot

data.Speed.plot(kind='line', color='g', label='Speed', linewidth=1, alpha=0.5, grid=True, linestyle=':')

data.Defense.plot(color='r', label='Defense', linewidth=1, alpha=0.5, grid=True, linestyle='-.')

plt.legend(loc='upper right')  #legend= puts label into plot
plt.xlabel('x axis')           #label= name of label
plt.ylabel('y axis')
plt.title('Line plot')         #Title= title of plot
plt.show()


# In[22]:


#Scatter Plot
#x=attack, y=defense

data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack Defense Scatter Plot')


# In[41]:


#Histogram
#bins= number of bar in figure

data.Speed.plot(kind='hist', bins=50, figsize=(12,12))
plt.show()


# In[42]:


#clf()= cleans it up again you can start a fresh
data.Speed.plot(kind='hist', bins=50)
plt.clf()
#we cannot see plot due to clf()


# In[43]:


#DICTIONARY
#Practice some other properties like keys(), values(), update, add, check, remove key, remove all entries, remove dictionary.

#1
#create dictionary and look its keys and values

dictionary={'spain': 'madrid', 'usa': 'vegas'}
print(dictionary.keys())
print(dictionary.values())


# In[ ]:









