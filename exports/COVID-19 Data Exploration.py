#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Data Exploration

# This notebook will load in a dataset of COVID-19 Community Mobility report data from Google and explore it using Python and popular python data science packages.

# ### Imports

# First let's load in some packages.

# In[1]:


from __future__ import print_function, division
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import HTML


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ### Data ingest

# Next let's load in the dataset into a panda's dataframe.

# In[3]:


df = pd.read_csv('../datasources/Global_Mobility_Report.csv', header=0, na_values = [''])
countries = pd.read_csv('../datasources/country-and-continent-codes-list-csv.csv')


# In[4]:


datetimes = ['date']
df = df.set_index('country_region_code').join(countries.set_index('Two_Letter_Country_Code'))
df[datetimes] = df[datetimes].apply(pd.to_datetime)


# In[5]:


sdf = df.sample(n = 50000)


# ### Let's explore!

# In[6]:


df


# In[7]:


df.info()


# In[8]:


df.describe()


# #### Single column exploration

# In[9]:


single_df = sdf['retail_and_recreation_percent_change_from_baseline']


# In[10]:


sns.displot(single_df, rug=True) 


# In[11]:


single_df.plot.box()


# ### Multi column data exploration

# In[12]:


multi_1_df = sdf['parks_percent_change_from_baseline']
multi_2_df = sdf['transit_stations_percent_change_from_baseline']
multi_df = sdf[['parks_percent_change_from_baseline', 'transit_stations_percent_change_from_baseline']].copy()


# In[13]:


multi_df.info()


# In[14]:


sns.jointplot(x=multi_1_df, y=multi_2_df, data=multi_df) 


# ### And now for the entire dataset...

# In[15]:


sns.pairplot(sdf, hue='Continent_Name', palette="husl") 


# In[16]:


corr = sdf.corr()
sns.heatmap(corr, xticklabels=True, yticklabels=True, cmap='RdBu') 

