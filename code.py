#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

#from subprocess import check_output
#print(check_output(["ls", "../ml"]).decode("utf8"))

import os
for dirname, _, filenames in os.walk("C:\\Users\EBRU\Documents\machineLearning"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# In[2]:
data= pd.read_csv('C:\\Users\EBRU\Documents\machineLearning\pokemon.csv')
data.head()

# In[3]:
data.info()


# In[4]:
data.corr()

# In[5]:
#correlation map
f,ax=plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.show()


# In[6]:
data.head(10)

# In[7]:
data.columns

# In[8]:
#line Plot

data.Speed.plot(kind='line', color='g', label='Speed', linewidth=1, alpha=0.5, grid=True, linestyle=':')

data.Defense.plot(color='r', label='Defense', linewidth=1, alpha=0.5, grid=True, linestyle='-.')

plt.legend(loc='upper right')  #legend= puts label into plot
plt.xlabel('x axis')           #label= name of label
plt.ylabel('y axis')
plt.title('Line plot')         #Title= title of plot
plt.show()

# In[9]:
#Scatter Plot
#x=attack, y=defense

data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack Defense Scatter Plot')

# In[10]:
#Histogram
#bins= number of bar in figure

data.Speed.plot(kind='hist', bins=50, figsize=(12,12))
plt.show()

# In[11]:
#clf()= cleans it up again you can start a fresh
data.Speed.plot(kind='hist', bins=50)
plt.clf()
#we cannot see plot due to clf()

# In[12]:
#DICTIONARY
#Practice some other properties like keys(), values(), update, add, check, remove key, remove all entries, remove dictionary.
#1
#create dictionary and look its keys and values
dictionary={'spain': 'madrid', 'usa': 'vegas'}
print(dictionary.keys())
print(dictionary.values())

# In[13]:
dictionary['spain']="barcelona"
print(dictionary)
dictionary['france']="paris"
print(dictionary)
del dictionary['spain']
print(dictionary)
print('france' in dictionary)
dictionary.clear()
print(dictionary)
print('france' in dictionary)
dictionary.clear()
print(dictionary)

# In[14]:
print(dictionary)

# In[15]:
data=pd.read_csv('C:\\Users\EBRU\Documents\machineLearning\pokemon.csv')

# In[16]:
series=data['Defense']
print(type(series))
data_frame=data[['Defense']]
print(type(data_frame))

# In[17]:
print(3>2)
print(3!=2)
print(True and False)
print(True or False)

# In[18]:
x=data['Defense']>200
data[x]

# In[19]:
data[np.logical_and(data['Defense']>200, data['Attack']>100)]

# In[20]:
data[(data['Defense']>200)&(data['Attack']>100)]

# In[21]:
i=0
while i!=5:
    print('i is:', i)
    i+=1
print(i, 'is equal to 5')

# In[22]:
lis=[1,2,3,4,5]
for i in lis:
    print('i is:', i)
print('')

for index, value in enumerate(lis):
    print(index,":", value)
print('')

dictionary={'spain':'madrid', 'france':'paris'}
for key, value in dictionary.items():
    print(key,":",value)
print('')

for index, value in data[['Attack']][0:1].iterrows():
    print(index,":",value)

# In[23]:
#2.PYTHON DATA SCIENCE TOOLBOX
#User Defined Function
#-Docstrings
#-Tuple

def tuple_ex():
    """return defined t tuple"""
    t=(1,2,3)
    return t
a, b, c= tuple_ex()
print(a, b, c)

# In[24]:
#-Scope
x=2            #global defination
def f():
    x=3        #local defination
    return x
print(x)       #-> this prints the global one
print(f())     #-> this prints the local one

# In[25]:
x=5
def f():
    y=2*x      #there are no x in local area so the x in global area is used
    return y
print(f())     

# In[26]:
import builtins
dir(builtins)

# In[27]:
#Nested Function
def square():
    """return square of value"""
    def add():
        """add two local variable"""
        x=2
        y=3
        z=x+y
        return z
    return add()**2
print(square())

# In[28]:
#Default and Flexible Arguments
#default arguments
def f(a, b=1, c=2):
    y= a+b+c
    return y
print(f(5))            # a->5  
print(f(5, 4, 3))      # a->5 , b->4, c->3

# In[29]:
#flexible arguments *args
def f(*args):
    for i in args:
        print(i)
f(1)
print("")
f(1, 2, 3, 4)
print("")

#flexible arguments **args
def f(**kwargs):
    """print key and value of dictionary"""
    for key, value in kwargs.items():
        print(key, " ", value)
f(country='spain', capital='madrid', population= 123456)

# In[30]:
#Lambda Function -> Faster way of writing function
square = lambda x: x**2
print(square(4))

tot = lambda x,y,z: x+y+z
print(tot(1,2,3))

# In[31]:
#Anonymous Function
number_list=[1,2,3]
y= map(lambda x:x**2, number_list)
print(list(y))

# In[32]:
#Iterators
name= "ronaldo"
it=iter(name)
print(next(it))     
print(*it)

# In[33]:
# zip(): zip lists
list1=[1,2,3,4]
list2=[5,6,7,8]
z=zip(list1, list2)
print(z)
z_list= list(z)       #z'yi liste halinde z_list'e atadık ve yazdırdık
print(z_list)

# In[34]:
# unzip list
un_zip= zip(*z_list)
un_list1, un_list2= list(un_zip) #unzip returns tuple
print(un_list1)
print(un_list2)
print(type(un_list1))
print(type(un_list2))

# In[35]:
#List Comprehension
num1=[1,2,3]
num2=[i+1 for i in num1]
print(num2)

# In[36]:
#conditionals on iterable (koşullu)
num1=[5,10,15]
num2=[i**2 if i==10 else i-5 if i<7 else i+5 for i in num1]
print(num2)

# In[37]:
threshold= sum(data.Speed)/len(data.Speed)    #average speed
data["speed_level"]=["high" if i> threshold else "low" for i in data.Speed]
data.loc[:10,["speed_level","Speed"]] 

# In[38]:
#3.CLEANING DATA
#Diagnose Data for Cleaning
data=pd.read_csv('C:\\Users\EBRU\Documents\machineLearning\pokemon.csv')
data.head()

# In[39]:
data.tail()
# In[40]:
data.columns
# In[41]:
data.shape
# In[42]:
data.info()
# In[43]:

#Exploratory Data Analysis
print(data['Type 1'].value_counts(dropna=False)) # if there are nan values that also be counted

# In[44]:

1,2,3,4,200

# In[45]:

data.describe()  #ignore null entries

# In[46]:

#Visual Exploratory Data Analysis

