#!/usr/bin/env python
# coding: utf-8

# STAT 7900 – Python for Data Science<br>
# Homework 3<br>
# Connor Armstrong<br>
# <br>
# 1. Create a CSV (Comma Separated Values) file from the data below (copy and paste the data into Excel then save as a csv) and read in as a Pandas Dataframe. Then do the following using Pandas operations that we covered in class (10 points): <br>

# In[5]:


import numpy as np
import pandas as pd
data = pd.read_csv('C:/Users/conno/OneDrive/Desktop/STAT 7900 - Python for Data Science/Homework/HW3 Data.csv')


# <br>
# a. What percent of records represent flowers? <br>
# The mean of the binary indicator variable is equivalent to the percentage of records which represent flowers. This parameter is calculated as follows:<br>

# In[4]:


percent_flowers = data['Flower'].mean()
percent_flowers


# Therefore, the percent of records which represent flowers is 45%.<br><br>
# b. What is the average Costs by Color?<br>

# In[24]:


costbycolor = pd.DataFrame(data['Cost'].groupby(data['Color']).mean())
costbycolor


# <br>c. Create a new column, that bins the Probability column into 4 equal frequency count bins (from low to high).<br>

# In[25]:


data['Bin'] = pd.qcut(data['Probability'], q=4)
data


# In[26]:


data['Bin'].value_counts()


# The column 'Bin' grouped the data into 4 equal frequency count bins as directed.<br><br>
# d. Create a crosstab of color and flower that represents the total cost.<br>

# In[31]:


pd.crosstab(data['Color'], data['Flower'], values=data['Cost'], aggfunc='sum', rownames=['Cost'], colnames=['Flower'])


# The dataframe above is a crosstab of color and flower which represents the total cost of each unique combination of the two.<br><br>
# e. Create a dataframe that contains flowers, only.<br>

# In[32]:


flowersonly = data[(data['Flower']== 1)]
flowersonly

