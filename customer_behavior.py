#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r'C:\Users\rakti\Downloads\customer_shopping_behavior.csv')


# In[4]:


df.head()


# In[5]:


df.info()


# In[7]:


df.describe(include='all')


# In[8]:


df.isnull().sum()


# In[10]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[11]:


df.isnull().sum()


# In[15]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})


# In[16]:


df.columns


# In[17]:


labels = ['Young Adult', 'Adult', 'Middle-ages', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)


# In[18]:


df[['age', 'age_group']].head(10)


# In[24]:


frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[25]:


df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)


# In[26]:


df = df.drop('promo_code_used', axis=1)


# In[27]:


pip install psycopg2-binary sqlalchemy


# In[31]:


from sqlalchemy import create_engine
username = "postgres"
password = "qwerty09"
host = "localhost"
port = "5432"
database = "customer_behavior"
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:




