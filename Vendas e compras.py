#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


vendas = pd.read_excel("base_vendas.xlsx")


# In[5]:


vendas.head(5)


# In[6]:


vendas.info()


# In[7]:


vendas.describe()


# In[4]:


pagamento = pd.read_excel("base_pagamentos.xlsx")


# In[9]:


pagamento.head(5)


# In[6]:


venda = pagamento[pagamento.payment_installments > 3]
venda.count()
round((28119)/(102528)*100,2)


# In[11]:


pagamento.payment_installments.count()


# In[12]:


pagamento.payment_value.mean()


# In[13]:


pagamento


# In[14]:


pagamento.payment_type


# In[15]:


pagamento.payment_type.value_counts()


# In[16]:


pagamento.payment_type.count()


# In[17]:


round((pagamento.payment_type.value_counts())/(pagamento.payment_type.count())*100,2)


# In[9]:


pagamento.groupby("payment_type")["payment_value"].mean().sort_values(ascending=False)


# In[19]:


transação = pagamento.groupby("payment_type")["payment_value"].sum().sort_values(ascending=False)
transação 


# In[18]:


pagamento.groupby("payment_type")["payment_value"].sum().sort_values(ascending=False).plot();


# In[17]:


pagamento.groupby("payment_type")["payment_value"].sum().sort_values(ascending=False).plot.bar();


# In[21]:


import matplotlib.pyplot as plt


# In[22]:


pagamento.groupby("payment_type")["payment_value"].sum().sort_values(ascending=False).plot.bar();
plt.savefig("transação",bbox_inches="tight",transparent=True)


# In[23]:


pagamento


# In[25]:


greater = pagamento[pagamento.payment_type == "credit_card"].groupby("payment_installments")["payment_value"].mean()
greater


# # teste
# 

# In[33]:


vendas.head(4)


# In[36]:


vendas.isnull().sum()


# In[39]:


vendas.loc[vendas.price.isnull(),"order_id"]


# In[38]:


ids = vendas.loc[vendas.price.isnull(),"order_id"].head(5)
pagamento[pagamento.order_id.isin(ids)]


# In[29]:


pagamento.loc[pagamento.order_id.isin(ids),"payment_value"].sum()


# In[30]:


venda[venda.order_id =="8e24261a7e58791d10cb1bf9da94df5c"]


# In[40]:


vendas  = vendas[vendas.price.notnull()]
vendas.head(3)


# In[34]:


vendas.isnull().sum()


# In[35]:


vendas[vendas.order_delivered_customer_date.isnull()]


# In[36]:


vendas.loc[vendas.order_delivered_customer_date.isnull(),"order_status"].value_counts()


# In[48]:


vendas = vendas[vendas.order_delivered_customer_date != "canceled"]


# In[49]:


vendas.isnull().sum()


# In[46]:


vendas = vendas.loc[vendas.product_category_name.isnull(),"product_category_name"] = "outros"


# In[47]:


vendas.isnull().sum()


# In[48]:


vendas


# In[124]:


vendas.groupby("order_purchase_timestamp")["price"].sum()


# In[52]:


vendas.groupby("order_purchase_timestamp")["price"].sum().plot();


# In[54]:


vendas.groupby("order_purchase_timestamp")["price"].sum().plot.box();


# In[57]:


import datetime as dt 


# In[131]:


vendas[vendas.order_purchase_timestamp >= dt.datetime(2017,11,1)].groupby("order_purchase_timestamp")["price"].sum().plot();


# In[67]:


vendas[(vendas.order_purchase_timestamp >= dt.datetime(2017,11,18)) &
      (vendas.order_purchase_timestamp <= dt.datetime(2017,11,27))
      ].groupby("order_purchase_timestamp")["price"].sum().plot();


# In[140]:


vendas = vendas[vendas.order_purchase_timestamp != dt.datetime(2017,11,1)]


# In[141]:


vendas[vendas.order_purchase_timestamp >= dt.datetime(2017,11,1)].groupby("order_purchase_timestamp")["price"].sum().plot();


# In[78]:


vendas.groupby("order_purchase_timestamp")["price"].sum().plot();


# In[145]:


vendas[(vendas.order_purchase_timestamp >= dt.datetime(2017,11,25)) &
      (vendas.order_purchase_timestamp <= dt.datetime(2017,11,30))
      ].groupby("order_purchase_timestamp")["price"].sum().plot();


# In[80]:


vendas = vendas[vendas.order_purchase_timestamp != dt.datetime(2017,11,25)]


# In[81]:


vendas.groupby("order_purchase_timestamp")["price"].sum().plot();


# In[85]:


vendas


# In[95]:


vendas.groupby("customer_state")["price"].sum().sort_values(ascending=False)


# In[91]:


vendas.groupby("customer_state")["price"].sum().sort_values(ascending=False).plot();


# In[93]:


vendas.groupby("customer_state")["price"].sum().sort_values(ascending=False).plot.bar();


# In[98]:


vendas


# In[101]:


vendas.groupby("product_category_name")["price"].count().sort_values(ascending=False)


# In[103]:


vendas.groupby("product_category_name")["price"].sum().sort_values(ascending=False)


# In[108]:


vendas.tail()


# In[106]:


categoria = "perfumaria"
vendas[vendas.product_category_name == categoria].groupby("order_purchase_timestamp")['price'].sum().plot();


# In[114]:


categoria = "bebes"
vendas[vendas.product_category_name == categoria].groupby("order_purchase_timestamp")["price"].sum().plot();


# In[ ]:





# In[ ]:




