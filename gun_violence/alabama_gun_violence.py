
# coding: utf-8

# In[15]:


import folium
import pandas as pd
import numpy as np


# In[2]:


gun_map = folium.Map(location=[32.3182, -86.9023], zoom_start=7)


# In[3]:


gun_data = pd.read_csv('al_gun_01.csv')


# In[4]:


gun_data.head()


# In[25]:


# build up datapoints
for i, row in gun_data.iterrows():
    if(not np.isnan(row['latitude'])):
        folium.Marker(location=[row['latitude'], row['longitude']],
                      popup="<a href=%s> INCIDENT INFO </a> \nNumber Killed:\t%d \n Number Injured:\t%d" %(row['incident_url'], row['n_killed'], row['n_injured'])).add_to(gun_map)

