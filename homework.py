
# coding: utf-8

# In[1]:


import json
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy
import pandas as pd
from __future__ import unicode_literals
get_ipython().magic('matplotlib inline')


# In[2]:


data = json.load(open("AQI.json"))


# In[3]:


type(data)


# In[4]:


print(data)


# In[5]:


newData = sorted(data, key=lambda k: k['SiteId'])


# In[6]:


print(newData)


# In[7]:


print (newData[6])


# In[8]:


newData1 = [x for x in newData if x['SiteId'] == '28']


# In[9]:


newJson = json.dumps(newData1, ensure_ascii=False)


# In[10]:


print (newJson)


# In[11]:


type(newJson)


# In[12]:


data2 = json.loads(newJson)


# In[13]:


type(data2)


# In[14]:


air_df = pd.DataFrame(data2)


# In[15]:


air_df


# In[16]:


print(data2)


# In[17]:


data2[0]


# In[18]:


print(data2[0]['AQI'])


# In[19]:


def getData():
    for value in data2:
        print('AQI:' + value['AQI'])
        print('Date:' + value['MonitorDate'])


# In[20]:


getData2 = []

for value in data2:
    getData2.append((value['MonitorDate'], value['AQI']))
    
getData2


# In[21]:


get_x = []

for x in getData2:
    get_x.append(x[0])
    
get_x

get_x1 = get_x
get_x1.reverse()

print (get_x1)

date_x = dates.datestr2num(get_x1)

print (date_x)


# In[22]:


get_y = []

for y in getData2:
    get_y.append(y[1])
    
get_y

"""反向排序"""
get_y1 = get_y
get_y1.reverse()

new_y = list(map(int, get_y1))

new_y


# In[23]:


"""plt.plot(new_y, label='AQI') <-你這個大笨蛋"""
plt.plot_date(date_x, new_y, 'b-', label="AQI", lw=2.5)
plt.fill_between(date_x, 50, interpolate=True, color='green', alpha=0.3)
plt.fill_between(date_x, 50, 100, interpolate=True, color='yellow', alpha=0.3)
plt.fill_between(date_x, 100, 150, interpolate=True, color='orange', alpha=0.3)
plt.fill_between(date_x, 150, 200, interpolate=True, color='red', alpha=0.3)
plt.fill_between(date_x, 200, 300, interpolate=True, color='purple', alpha=0.3)


y_max = max(new_y)

plt.plot(date_x[-2], y_max, marker='o', markersize=8, color="red")

plt.gcf().autofmt_xdate(rotation=30)


plt.xlabel('Date')
plt.ylabel('AQI')

plt.ylim((0, 300))

plt.title("Air Quality Index in Fengyuan")
plt.legend(loc='upper right', prop={'size': 13})

plt.show()

