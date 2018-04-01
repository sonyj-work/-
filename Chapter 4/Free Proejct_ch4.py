
# coding: utf-8

# In[1]:


def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    
    return result


# In[2]:


def square(sequence):
    result = []
    for element in sequence:
        result = result + [element * element]
    
    return result


# In[3]:


square([1, 2, 3])

