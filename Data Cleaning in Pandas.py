#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd


# In[36]:


df = pd.read_excel(r"C:\Users\Mustafa\Downloads\SQL Project\Customer Call List.xlsx")
df


# In[37]:


df = df.drop_duplicates()
df


# In[38]:


df = df.drop(columns = "Not_Useful_Column")


# In[39]:


df


# In[40]:


df["Last_Name"] = df["Last_Name"].str.strip("/")
df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df


# In[46]:


#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10] + '-')
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
#df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# In[52]:


df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',2, expand = True)
df


# In[55]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')
df


# In[57]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df


# In[66]:


df = df.replace('N/a','')
df = df.fillna('')
df


# In[67]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace = True)
df


# In[68]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace = True)
df


# In[71]:


df = df.drop(columns = "Address")


# In[72]:


df


# In[74]:


df.reset_index(drop = True)


# In[75]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




