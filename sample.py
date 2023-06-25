#!/usr/bin/env python
# coding: utf-8

# In[1]:


path2019 = r"C:\Users\HP\Desktop\sample.xlsx"
import pandas as pd
import datetime as dt
df2 = pd.read_excel(path2019)
df2


# In[2]:


df2['Date_s']=pd.to_datetime(df2.Date_s, format='%d-%m-%Y %H:%M')
df2['Date_e']=pd.to_datetime(df2.Date_e, format='%d-%m-%Y %H:%M')
df2


# In[3]:


df2["Time_s"]=df2["Date_s"].dt.time
df2["Time_e"]=df2["Date_e"].dt.time


# In[4]:


df2["Date_s"]=df2["Date_s"].dt.date
df2["Date_e"]=df2["Date_e"].dt.date


# In[5]:


df2['Time_s']=pd.to_datetime(df2.Time_s, format='%H:%M:%S')
df2['Time_e']=pd.to_datetime(df2.Time_e, format='%H:%M:%S')


# In[17]:


df2["Hour_s"]=df2['Time_s'].dt.strftime("%H")
df2["Hour_e"]=df2['Time_e'].dt.strftime("%H")
df2


# In[18]:


ozone1= df2.Ozone
print(ozone1)


# In[22]:


a= len(df2.Hour_s)
print(a)
b = [ ]
for i in range (a):
    x= int ( df2.Hour_s[i] )
    b = b + [x]
print(b)
print(x)


# In[9]:


z=0
l=len(b)
for i in range (l):
    if b[i]>= 9 and b[i]<= 16 :
        d= ozone1[i]
        z= z+d
print('M7 is equal to',z)


# In[16]:


x= int(len(ozone1))
a=0
for i in range (x):
    if ozone1[i]> 40:
        d= ozone1[i]
        a=a+d
print('AOT40 is equal to',a)
print("d",d)


# In[ ]:





# In[ ]:




