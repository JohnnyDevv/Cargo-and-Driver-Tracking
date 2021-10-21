#!/usr/bin/env python
# coding: utf-8

# ## EXTRACTION AND CLEANING OF AUTOMOTIVE DATASET FROM FLO CONCEPT LTD

# In[1]:


#import pandas package
import pandas as pd

#import dataset
df = pd.read_excel('Rohit.xlsx', header=0, sep=',', engine='openpyxl')

#print first 5 rows
print(df.head())


# In[2]:


#check info of data
df.info()


# #### Dataset Description
#      VIN is the unique ID of each car.
#      Each car is attached to one Tour.
#      Each tour starts somewhere and ends somewhere, and is dated.
#      Each car has a CEU number associated with it.
#      So each tour has a CEU - being the sum of the CEUs of the cars on it.

# #### Goal
#      We're interested in the average CEU per tour... and whether the CEU per tour changes depending on the day of the week,      week of the month, or month of the year.
#      
#      We're also interested in where the drivers end up each week - they should leave their home/base on a Monday and come        back to/close to that home/base every Friday. Home/base could be NVD Ringaskiddy, NVD Rosslare, NVD Baldonnell, NVD        Kill, Dublin Port.
#      
#      Lastly, we'll try to see if there are patterns of interest in how the tours that they are driving might change shape        towards the end of the week.

# In[3]:


#create a new column that computes average CEU per tour
df['Avg_CEU_per_tour'] = df['CEU'].mean()/df['Tour']

#print first 5 rows of this new column
print(df['Avg_CEU_per_tour'].head())


# #### We're interested in keeping these columns: Driver, Start Location, Target Location, Start Date, End Date, Tour, Final Location, Target Delivery Time, Order Time, Truck, startedby and completedby. We will drop the rest.

# In[4]:


columns_to_use = ['Driver', 'Start Location', 'Target Location', 'Start Date', 'End Date', 'Tour', 'Final Location', 
                  'Target Delivery Time', 'Order Time', 'startedby', 'completedby', 'Avg_CEU_per_tour']

#use a for loop to delete other columns
for i in df.columns:
    if i not in columns_to_use:
        df = df.drop([i], axis=1)


# In[5]:


df.info()


# In[6]:


df.head()


# #### Notice the values for Start Date,	End Date, Target Delivery Time and Order Time consist of date and time. Let's split them in individual dates and times.

# In[7]:


#splitting the date & time columns
df[['start date', 'start time']] = df['Start Date'].str.split('T', expand=True)
df[['end date', 'end time']] = df['End Date'].str.split('T', expand=True)
df[['target delivery date', 'target delivery time']] = df['Target Delivery Time'].str.split('T', expand=True)
df[['order date', 'order time']] = df['Order Time'].str.split('T', expand=True)


# In[8]:


df.head()


# In[9]:


#check no. of columns
df.shape[1]


# In[10]:


#deleting Start Date, End Date, Target Delivery Time and Order Time columns
df = df.drop(['Start Date', 'End Date', 'Target Delivery Time', 'Order Time'], axis=1)

#no. of columns should have reduced by 4
df.shape[1]


# In[11]:


#check for null values
df.isna().sum()


# In[12]:


#Let's inspect the dataframe where Driver is null
df[df['Driver'].isnull()]


# In[13]:


#drop rows that contain null values
df.dropna(axis=0, inplace=True)


# In[14]:


#making sure sum of all null values in dataframe is zero
df.isnull().sum().sum()


# In[15]:


#check updated dimension of data
df.shape


# In[16]:


#inspect datatypes of each column
df.dtypes


# In[17]:


#export cleaned and modified data to excel file
df.to_excel(r'C:\Users\John Uzoma\Documents\data analytics projects\cargo&driver_tracking\cleaned_Rohit.xlsx', index=False)


# ## Click the link in the ReadMe section to view Tableau visualizations.
