#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.DataFrame()
print(df)


# In[10]:


emp=pd.Series(["a","b","c","d","e"])
idt=pd.Series([10,20,30,40,50])
f={'emp':emp,'idt':idt}
r=pd.DataFrame(f)
print(r)


# In[16]:


#Extracting a colum
print(r['emp'])


# In[18]:


#Adding a new column
r["Age"]=pd.Series([20,35,25,45,32])
print(r)


# In[20]:


#delete an existing column
del r['Age']
print(r)


# In[21]:


#slicing of rows
print(r[1:3])


# In[32]:


# addition of rows
emp=pd.Series(["a","b","c","d","e"])
idt=pd.Series([10,20,30,40,50])
f={'emp':emp,'idt':idt}
r=pd.DataFrame(f)
print(r)
d2=pd.DataFrame([['f',67],['g',69]],columns=['emp','idt'])
print(pd.concat([r,d2]))


# In[33]:


#delete an existing row
print(r.drop(2))

