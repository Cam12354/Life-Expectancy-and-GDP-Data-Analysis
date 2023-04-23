#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[6]:


pd.read_csv("all_data.csv")


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


plt.title('Country - Chile')

plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [77,70,69,75,99,122,154,173,179,172,218,252,267,278,260,242])
plt.ylabel('GDP in  terms of Billions')
plt.xlabel('Year')
plt.show()



plt.title('Country - Chile')

plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [77.3,77.3,77.8,77.9,78,78.4,78.9,78.9,79.6,79.3,79.1,79.8,79.9,80.1,80.3,80.5])
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('Year')
plt.show()

plt.title('Country - Chile')

plt.plot([77.3,77.3,77.8,77.9,78,78.4,78.9,78.9,79.6,79.3,79.1,79.8,79.9,80.1,80.3,80.5], [77,70,69,75,99,122,154,173,179,172,218,252,267,278,260,242],)
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('GDP in  terms of Billions')
plt.show()


# In[6]:


# Analyzing this data set can allow us to concur that GDP has a huge factor and impact on a country's Life Expectancy rate at Birth.
# We can also concur that as GDP increases, the Life Expectancy Rate at Birth increases as well. 
# However, it is important to note that other factors such as cultural, environmental, 
# and social conditions also play a significant role in determining life expectancy
# and that simply having a high GDP does not guarantee a high life expectancy rate.

def Average(gdp):
    avg = np.average(gdp)
    return(avg)
gdp = [77,70,69,75,99,122,154,173,179,172,218,252,267,278,260,242]



print("This data set has a mean GDP of ",round(Average(gdp),2), "billion")


def Average(ler):
    avg = np.average(ler)
    return(avg)
ler = [77.3,77.3,77.8,77.9,78,78.4,78.9,78.9,79.6,79.3,79.1,79.8,79.9,80.1,80.3,80.5]

print("This data set has a mean Life Expectancy Rate of",round(Average(ler), 2), "years")


# In[7]:


plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [77,70,69,75,99,122,154,173,179,172,218,252,267,278,260,242])
plt.ylabel('GDP in  terms of Billions')
plt.xlabel('Year')
plt.show()





plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [77.3,77.3,77.8,77.9,78,78.4,78.9,78.9,79.6,79.3,79.1,79.8,79.9,80.1,80.3,80.5])
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('Year')
plt.show()



plt.plot([77.3,77.3,77.8,77.9,78,78.4,78.9,78.9,79.6,79.3,79.1,79.8,79.9,80.1,80.3,80.5], [77,70,69,75,99,122,154,173,179,172,218,252,267,278,260,242],)
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('GDP in  terms of Billions')
plt.show()


# In[8]:


plt.title('Country - China')

plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [1.2,1.3,1.47,1.6,1.95,2.2,2.7,3.5,4.5,5.1,6.1,7.5,8.5,9.6,10.4,11])
plt.ylabel('GDP in  terms of Trillions')
plt.xlabel('Year')
plt.show()



plt.title('Country - China')

plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [71,72.2,72.7,73.1,73.5,73.9,74.2,74.4,74.5,74.9,75,75.2,75.4,75.6,75.8,76.1])
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('Year')
plt.show()

plt.title('Country - China')

plt.plot([1.2,1.3,1.47,1.6,1.95,2.2,2.7,3.5,4.5,5.1,6.1,7.5,8.5,9.6,10.4,11], [71,72.2,72.7,73.1,73.5,73.9,74.2,74.4,74.5,74.9,75,75.2,75.4,75.6,75.8,76.1],)
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('GDP in  terms of Trillions')
plt.show()


# In[11]:


plt.title('Country - Zimbabwe')

plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [6.6, 6.7, 6.3, 5.7, 5.8, 5.75, 5.4, 5.2, 4.4, 8.6, 10.1, 12.0, 14, 15.4, 15.8, 16.3])
plt.ylabel('GDP in  terms of Billions')
plt.xlabel('Year')
plt.show()



plt.title('Country - Zimbabwe')

plt.plot([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], [46, 45.3, 44.8, 44.5, 44.3, 44.6, 45.4, 46.6, 48.2, 50.0, 52.4, 54.9, 56.6, 58, 59.2, 60.7])
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('Year')
plt.show()

plt.title('Country - Zimbabwe')

plt.plot([46, 45.3, 44.8, 44.5, 44.3, 44.6, 45.4, 46.6, 48.2, 50.0, 52.4, 54.9, 56.6, 58, 59.2, 60.7], [6.6, 6.7, 6.3, 5.7, 5.8, 5.75, 5.4, 5.2, 4.4, 8.6, 10.1, 12.0, 14, 15.4, 15.8, 16.3],)
plt.ylabel('Life Exp at Brth in terms of years')
plt.xlabel('GDP in  terms of Billions')
plt.show()


# In[ ]:




