#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas package
import pandas as pd

#import dataset
car_data = pd.read_excel('Rohit.xlsx', header=0, sep=',', engine='openpyxl')

#print first 5 rows
print(car_data.head())


# In[2]:


#check info of data
car_data.info()


# In[3]:


#delete irrelevant columns
car_data.drop(car_data.columns[[1,2,3,4,7,8,9,10,11,12,13,16,17,18,19,20,21,23,24,26,27,28,30,31,32,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]], axis=1, inplace=True)


# In[4]:


car_data.info()


# In[5]:


#check for nan values
car_data.isna().sum()


# In[6]:


#drop rows that contain nan values
car_data.dropna(axis=0, inplace=True)


# In[7]:


#check updated dimension of data
car_data.shape


# In[8]:


#create a new column that computes average CEU per tour
car_data['Avg_CEU_per_tour'] = car_data['CEU'].mean()/car_data['Tour']

#print first 5 rows of this new column
print(car_data['Avg_CEU_per_tour'].head())


# In[9]:


#export cleaned and modified data to CSV file
car_data.to_csv(r'C:\Users\John Uzoma\Documents\DBS_MASTERS\miscellaneous\data_science\datasets\modified_Rohit.csv', index=False)

