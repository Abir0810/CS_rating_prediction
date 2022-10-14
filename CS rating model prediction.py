#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel(r"E:\I sharify/CS_Rating_model.xlsx")


# In[3]:


df.head(2)


# In[4]:


from sklearn import linear_model


# In[5]:


from sklearn.linear_model import LinearRegression


# In[6]:


reg=LinearRegression()


# In[7]:


y = df[['rating']]
x = df.drop(['rating'],axis=1)
x=x.dropna()


# In[8]:


from sklearn.model_selection import train_test_split


# In[9]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=10)


# In[10]:


from sklearn.linear_model import LinearRegression


# In[11]:


logmodel=LinearRegression()


# In[12]:


logmodel.fit(x_train, y_train)


# In[13]:


x_train


# In[17]:


logmodel.predict([[56.6,8.8]])


# In[15]:


logmodel.score(x_test,y_test)


# In[16]:


logmodel.coef_


# In[17]:


logmodel.intercept_


# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


from sklearn.gaussian_process import GaussianProcessRegressor


# In[19]:


gpr = GaussianProcessRegressor()


# In[20]:


gpr.fit(x_train,y_train)


# In[21]:


gpr.fit(x_train, y_train)


# In[22]:


gpr.predict([[70,7.2]])


# In[23]:


gpr.score(x_test,y_test)


# In[ ]:





# In[18]:


import matplotlib.pyplot as plt


# In[19]:


a = ['Week-38','Week-39']


# In[20]:


b = [4.7,4.8]


# In[21]:


c=[8.4,8.8]


# In[22]:


d=[51.5,56.6]


# In[ ]:





# In[23]:


plt.bar(a,b, color=('Red','Red'))
plt.ylabel("")
plt.xlabel("")

plt.title("Customer service Rating")
plt.show()


# In[24]:


plt.bar(a,c, color=('Orange','Orange'))
plt.ylabel("")
plt.xlabel("")

plt.title("Average Response Time")
plt.show()


# In[26]:


plt.bar(a,d, color=('Red','Orange'))
plt.ylabel("")
plt.xlabel("")

plt.title("First Contact Resolution Rate")
plt.show()


# In[ ]:





# In[ ]:




