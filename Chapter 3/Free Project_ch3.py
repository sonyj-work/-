
# coding: utf-8

# In[1]:


def triple(sequence):
    result = []
    for element in sequence:
        result = result + [element * 3]
    return result


# In[2]:


triple([1, 2, 3])

