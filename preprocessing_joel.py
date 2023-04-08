#!/usr/bin/env python
# coding: utf-8

# # Load Data from Default s3 Bucket & Preprocessing data for Athena

# ### Get default bucket name

# In[16]:


import sagemaker
bucket = sagemaker.Session().default_bucket()
print(bucket)


# ### View Bucket Contents
# ##### NOTE the data was manually placed into bucket using AWS s3 UI

# In[17]:


get_ipython().run_cell_magic('bash', '', '\naws s3 ls s3://sagemaker-us-east-1-418795740224/csv/\n')


# ### Load CSV files in s3 into pandas dataframes

# In[18]:


import pandas as pd
ca = pd.read_csv("s3://{}/csv/CA_youtube_trending_data.csv".format(bucket))
gb = pd.read_csv("s3://{}/csv/GB_youtube_trending_data.csv".format(bucket))
us = pd.read_csv("s3://{}/csv/US_youtube_trending_data.csv".format(bucket))


# ### Create Location column

# In[19]:


us.insert(0, 'Location',  'US')
gb.insert(0, 'Location',  'GB')
ca.insert(0, 'Location',  'CA')
print(len(us), len(gb), len(ca))


# ### Combine pandas dataframes

# In[20]:


usgb = us.append(gb, ignore_index=True)
finalcsv = usgb.append(ca, ignore_index=True)
print(len(finalcsv))


# # Format Data using Pandas within Sagemaker 
# ##### Parsing issues when inserting data into Athena rquires pre-processing of csv files upon upload

# ### Null Values
# ##### The only null values are found witin the description column

# In[21]:


print(finalcsv.isnull().sum())


# ### Duplicate values
# ##### Because videos can trend multiple times, it is imprtaint to remove duplicates

# In[22]:


finalcsv.drop_duplicates('video_id', keep = 'last', inplace = True)
print(len(finalcsv))


# # Feature Creation
# ##### Athena had trouble parsing the description and tags columns - so lets create features which capture some value from what we have without needing to upload the entire column data

# ### description_length
# ##### Description is troublesome both because of parsing errors with athena but also because of the presence of duplicate values
# ##### To solve this let smake a new column called description length which will replace null columns with 0 as well as provide insight into how long description length is for trending videos
# ##### The disadvantage of this step is losing out on the the substance of the description itself, but advantages outweigh the costs here

# In[25]:


finalcsv['description_length']  = finalcsv['description'] .str.len()
finalcsv.head(3)


# ### timepublished
# ##### Using the publishedAT create a new column that provides only the hour of the day the video was origonally published

# In[40]:


#finalcsv['publishedAt']  = finalcsv['publishedAt'].astype(str)
finalcsv['timepublished']  = finalcsv['publishedAt'].str[11:13]
finalcsv.head(3)


# ### trending_month & trending_year
# ##### Using the Trending date lets make two new columns that capture the month and year of the last day it was trending
# ##### NOTE When duplicates were removed, only the latest instance was kept
# ##### The data includes instances from 08/2020 to 03/2023

# In[41]:


finalcsv['trending_month']  = finalcsv['trending_date'].str[5:7]
finalcsv['trending_year']  = finalcsv['trending_date'].str[:4]
finalcsv.head(3)


# # Reformat 'tags' 'title' and 'channelTitle' features
# ##### the Tags feature also presented a problem with athena
# ##### One solution i found is to just strip all of the character from the column so that it is an uninterupted string for each instance

# In[26]:


def strip(x):
    #removes all the formatting so I can search against a "clean" list
    x = x.str.replace(' ','', regex=True).str.replace('.','', regex=True).str.replace(',','', regex=True).str.replace('|','', regex=True).str.replace("'",'', regex=True).str.replace('-',"", regex=True).str.replace("(",'', regex=True).str.replace(')',"", regex=True).str.replace('/',"", regex=True).str.replace('â„¢',"", regex=True).str.replace('â‚¬',"", regex=True).str.replace('Ã¢',"", regex=True).str.replace('&',"", regex=True).str.lower().str.replace('-',"", regex=True).str.replace('&',"", regex=True)
    return x


# In[46]:


finalcsv['tags'] = strip(finalcsv['tags'])
finalcsv['title'] = strip(finalcsv['title'])
finalcsv['channelTitle'] = strip(finalcsv['channelTitle'])


# ### Remove unneccessary features
# ##### In this case it is the columns containing ambiguous ID values as well as the thumbnail link
# ##### Dont forget about the description and tags columns too - they got to go

# In[44]:


droplist = ['thumbnail_link', 'channelId','video_id', 'description', 'publishedAt', 'trending_date']
for col in finalcsv.columns:
    if col in droplist:
        finalcsv.drop(col, axis='columns', inplace=True)


# # Change DataTypes

# In[48]:


finalcsv.dtypes


# In[ ]:





# ### Save final CSV to its own folder in bucket then Store

# In[47]:


finalcsv.head(5)


# In[49]:


get_ipython().run_line_magic('store', 'finalcsv')


# In[ ]:




