#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return ways(n - 1) + ways(n - 2) + ways(n - 3)


# In[ ]:




