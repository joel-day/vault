#!/usr/bin/env python
# coding: utf-8

# ### Create an AWS bucket
# ##### The bucket name cannot contain underscores, end with a dash, have consecutive periods, or use dashes adjacent to periods. The bucket name cannot be formatted as an IP address (198.51. 100.24).
# ##### Bucket name MUST CONATIN the string 'sagemaker' to qualify as a default bucket in Sagemaker

# In[2]:


import boto3
bucketname = 'sagemakerviewboost'
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket=bucketname)

#!aws s3api create-bucket --bucket viewboostyoutubejoel --region us-east-1


# ### List all Buckets to ensure new bucket was created

# In[3]:


get_ipython().run_cell_magic('bash', '', '\naws s3 ls s3://${bucket}/\n')


# ### Set the new bucket as default

# In[4]:


import sagemaker
sess = sagemaker.Session()
bucket = bucketname
print(bucket)


# ### Verify Bucket is Default

# In[5]:


print("Default bucket: {}".format(bucket))


# # Manually add data to s3 Bucket

# ### Make sure data is in bucket

# In[6]:


get_ipython().run_cell_magic('bash', '', '\naws s3 ls s3://sagemakerviewboost/\n')


# ### Load CSV files in s3 into pandas dataframes

# In[7]:


import pandas as pd
ca = pd.read_csv("s3://sagemaker-us-east-1-418795740224/data/CA_youtube_trending_data.csv")
gb = pd.read_csv("s3://sagemaker-us-east-1-418795740224/data/GB_youtube_trending_data.csv")
us = pd.read_csv("s3://sagemaker-us-east-1-418795740224/data/US_youtube_trending_data.csv")


# ### Create Location column

# In[8]:


us.insert(0, 'Location',  'US')
gb.insert(0, 'Location',  'GB')
ca.insert(0, 'Location',  'CA')
print(len(us), len(gb), len(ca))


# ### Combine csv's

# In[16]:


usgb = us.append(gb, ignore_index=True)
finalcsv = usgb.append(ca, ignore_index=True)
print(len(finalcsv))


# In[10]:


finalcsv.head(3)


# ### Get all column names

# In[11]:


my_list = finalcsv.columns.values.tolist()
print(my_list)


# ### Drop irrelevant columns

# In[12]:


droplist = ['thumbnail_link', 'channelId','video_id']
for col in finalcsv.columns:
    if col in droplist:
        finalcsv.drop(col, axis='columns', inplace=True)


# In[13]:


finalcsv.head(3)


# ### Store Pandas dataframe using store

# In[1]:


get_ipython().run_line_magic('store', 'finalcsv')

