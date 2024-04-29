#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("C:\\Users\\sonal\\Downloads\\Diwali Sales Data.csv", encoding='unicode_escape')
# use Unicodeesacpe to avoid error & again if not load then apply two slashes \\ 


# In[6]:


df.shape


# In[7]:


df.head(10)


# In[33]:


df.info()


# In[34]:


df.drop(['Status','unnamed1'],axis = 1, inplace = True)
# to drop unused columns


# In[35]:


df.head(10)


# In[36]:


pd.isnull(df)


# In[37]:


pd.isnull(df).sum()


# In[38]:


df.dropna(inplace=True)


# In[40]:


pd.isnull(df).sum()


# In[50]:


# Change the data type
df["Amount"] = df["Amount"].astype('int')


# In[51]:


df["Amount"].dtypes


# In[52]:


df.columns


# In[53]:


df.rename(columns = {"Marital_Status" : "Shadi"})


# In[54]:


df.describe()


# In[55]:


df[["Marital_Status","Amount","Age"]].describe()


# # Exploratory Data Analysis

# Gender

# In[61]:


ax = sns.countplot(x = 'Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[64]:


df.groupby(["Gender"], as_index  = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)


# In[67]:


sales_gen=df.groupby(["Gender"], as_index  = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.barplot(x="Gender", y = "Amount", data = sales_gen)


# Female purchases more products than mens

# Age

# In[71]:


ax = sns.countplot(data = df, x = "Age Group",hue = "Gender")

for bars in ax.containers:
    ax.bar_label(bars)


# In[72]:


sales_age=df.groupby(["Age Group"], as_index  = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.barplot(x="Age Group", y = "Amount", data = sales_age)


# From above Graph we can see that most of the buyers are from age group 26-35 years females

# state

# In[73]:


df.columns


# In[77]:


sales_state=df.groupby(["State"], as_index  = False)["Orders"].sum().sort_values(by = "Orders", ascending = False).head(10)
sns.set(rc={"figure.figsize":(15,6)})
sns.barplot(x="State", y = "Orders", data = sales_state)


# above bar graph using head to see top 10 states

# We can see that most of the orders are from UttarPradesh, Maharashtra and Karnatka

# Marital status

# In[80]:


ax = sns.countplot(data = df, x = "Marital_Status")
sns.set(rc={"figure.figsize":(2,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[84]:


sales_marries=df.groupby(["Marital_Status","Gender"], as_index  = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)
sns.set(rc={"figure.figsize":(6,5)})
sns.barplot(x="Marital_Status", y = "Amount", data = sales_marries,hue = "Gender")


# as per the above chart married womens has spent huge amount on shopping 

# OCCUPATION

# In[85]:


df.columns


# In[91]:


sns.set(rc={"figure.figsize":(20,5)})
ax = sns.countplot(data = df, x = "Occupation")

for bars in ax.containers:
    ax.bar_label(bars)


# In[92]:


sales_occupations=df.groupby(["Occupation"], as_index  = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.set(rc={"figure.figsize":(20,5)})
sns.barplot(x="Occupation", y = "Amount", data = sales_occupations)


# We can see Top two sectors who's purchasing power is more  = IT sector & Healthcare 

# Product Category

# In[93]:


df.columns


# In[95]:


sns.set(rc={"figure.figsize":(25,5)})
ax = sns.countplot(data = df, x = "Product_Category")

for bars in ax.containers:
    ax.bar_label(bars)


# In[96]:


sales_product=df.groupby(["Product_Category"], as_index  = False)["Amount"].sum().sort_values(by = "Amount", ascending = False).head(10)

sns.set(rc={"figure.figsize":(20,5)})
sns.barplot(x="Product_Category", y = "Amount", data = sales_product)


# most sold products are food, clothing and electronics

# In[97]:


df.columns


# In[98]:


sales_productd=df.groupby(["Product_ID"], as_index  = False)["Orders"].sum().sort_values(by = "Orders", ascending = False).head(10)

sns.set(rc={"figure.figsize":(20,5)})
sns.barplot(x="Product_ID", y = "Orders", data = sales_productd)


# # Conclusion

# Married woman age group between 26-35 yrs from UP, Maharashtra & Karnataka working in IT, Healthcare and Aviation 
# are more likely to buy products from Food ,Clothing and Electronics category 

# Thank You
