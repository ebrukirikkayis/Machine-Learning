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


# In[ ]:




