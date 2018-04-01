
# coding: utf-8

# In[1]:


def positive(sequence):
    length = 0
    for element in sequence:
        if element > 0:
            length = length + 1


# In[2]:


def positive(sequence):
    length = 0
    
    for element in sequence:
        if element > 0:
            length = length + 1
    
    return length


# In[3]:


positive([1, -1, 3, -5, 8])


# In[4]:


def positive(sequence):
    length = len(sequence)
    for element in sequence:
        if element <= 0
            length = length - 1
    
    return length


# In[5]:


def positive(sequence):
    length = len(sequence)
    for element in sequence:
        if element <= 0:
            length = length - 1
    
    return length


# In[6]:


positive([1, -1, 3, -5, 8])


# In[7]:


def pluses(sequence):
    result = sum(sequence)
    for element in sequence:
        if element <= 0:
            result = result - element
    
    return result


# In[8]:


pluses([1, -1, 3, -5 ,8])

