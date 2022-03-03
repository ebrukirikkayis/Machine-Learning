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
data.boxplot(column='Attack', by='Legendary')

# In[47]:
data_new=data.head()
data_new

# In[48]:
melted=pd.melt(frame=data_new, id_vars='Name', value_vars=['Attack','Defense'])
melted

# In[49]:
#PIVOTING DATA
melted.pivot(index='Name', columns='variable', values='value')

# In[50]:
data1=data.head()
data2=data.tail()
conc_data_row=pd.concat([data1, data2], axis=0, ignore_index=True)
conc_data_row

# In[51]:
data1=data['Attack'].head()
data2=data['Defense'].head()
conc_data_col=pd.concat([data1,data2],axis=1)
conc_data_col

# In[52]:
#Data Types
data.dtypes
data['Type 1']=data['Type 1'].astype('category')
data['Speed']=data['Speed'].astype('float')

# In[53]:
data.dtypes

# In[54]:
#Missing data and testing with assert
data.info()

# In[55]:
data["Type 2"].value_counts(dropna=False)

# In[56]:
data1=data
data1["Type 2"].dropna(inplace=True)

# In[57]:
assert 1==1

# In[58]:
#assert data['Type 2'].notnull().all() #returns nothing because we drop nan values

# In[59]:
data["Type 2"].fillna('empty', inplace=True)

# In[60]:
assert data['Type 2'].notnull().all()

# In[61]:
#PANDAS
#data frames from dictionary
country=["Spain","France"]
population=["11","12"]
list_label=["country","population"]
list_col=[country,population]
zipped=list(zip(list_label,list_col))
data_dict=dict(zipped)
df=pd.DataFrame(data_dict)
df

# In[62]:
df["capital"]=["madrid","paris"]
df

# In[63]:
df["income"]=0
df

# In[64]:
#Visual exploratory data analysis
data1=data.loc[:,["Attack","Defense","Speed"]]
data1.plot()

# In[65]:
data1.plot(subplots=True)
plt.show()

# In[66]:
data1.plot(kind="scatter",x="Attack",y="Defense")
plt.show()

# In[67]:
#data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)

# In[68]:
#fig, axes = plt.subplots(nrows=2,ncols=1)
#data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[0])
#data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[1],cumulative = True)
#plt.savefig('graph.png')
#plt

# In[69]:
data.describe()

# In[70]:
time_list=["1992-03-08","1992-04-12"]
print(type(time_list[1]))
datetime_object=pd.to_datetime(time_list)
print(type(datetime_object))

# In[71]:
import warnings
warnings.filterwarnings("ignore")
data2=data.head()
date_list=["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object=pd.to_datetime(date_list)
data2["date"]=datetime_object
data2=data2.set_index("date")
data2


# In[72]:
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])

# In[73]:
#Resampling Pandas Time Series
data2.resample("A").mean()

# In[74]:
data2.resample("M").mean()

# In[75]:
#data2.resample("M").first().interpolate("linear")

# In[76]:
data2.resample("M").mean().interpolate("linear")

# In[77]:
data=pd.read_csv('C:\\Users\EBRU\Documents\machineLearning\pokemon.csv')
data=data.set_index("#")
data.head()

# In[78]:
data["HP"][1]

# In[79]:
data.HP[1]

# In[80]:
data.loc[1,["HP"]]

# In[81]:
data[["HP","Attack"]]

# In[82]:
#Slicing Data Frame
print(type(data["HP"]))       #series
print(type(data[["HP"]]))     #data frames

# In[83]:
data.loc[1:10,"HP":"Defense"]

# In[84]:
data.loc[10:1:-1,"HP":"Defense"]

# In[85]:
data.loc[1:10,"Speed":]

# In[86]:
#Filtering Data Frames
#Creating boolean series
boolean=data.HP>200
data[boolean]

# In[87]:
first_filter=data.HP>150
second_filter=data.Speed>35
data[first_filter & second_filter]

# In[88]:
#filtering column based others
data.HP[data.Speed<15]

# In[89]:
#transforming data
def div(n):
    return n/2
data.HP.apply(div)

# In[90]:
data.HP.apply(lambda n: n/2)

# In[91]:
#Defining column using other columns
data["total_power"]=data.Attack+data.Defense
data.head()

# In[92]:
#Index objects and labeled data
print(data.index.name)
data.index.name="index_name"
data.head()

# In[93]:
data.head()
data3=data.copy()
data3.index=range(100,900,1)
data3.head()

# In[94]:
#Hierarchical Indexing
data=pd.read_csv('C:\\Users\EBRU\Documents\machineLearning\pokemon.csv')
data.head()

# In[95]:
data1= data.set_index(["Type 1","Type 2"])
data1.head(100)

# In[96]:
#Pivoting Data Frames
dic={"treatment":["A","A","B","B"],"gender": ["F","M","F","M"], "response":[10,45,5,9], "age":[15,4,72,65]}
df=pd.DataFrame(dic)
df

# In[97]:
df.pivot(index="treatment", columns="gender", values="response")

# In[98]:
#Stacking and Unstacking Dataframe
df1=df.set_index(["treatment","gender"])
df1

# In[99]:
df1.unstack(level=0)

# In[100]:
df1.unstack(level=1)

# In[101]:
df2=df1.swaplevel(0,1)
df2

# In[102]:
#Melting Data Frames
df

# In[103]:
pd.melt(df, id_vars="treatment", value_vars=["age","response"])

# In[104]:
#Categoricals and groupby
df
# In[105]:
df.groupby("treatment").mean()

# In[106]:
df.groupby("treatment").age.max()

# In[107]:
df.groupby("treatment")[["age","response"]].min()

# In[108]:
df.info()



