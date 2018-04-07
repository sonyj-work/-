
# coding: utf-8

# In[1]:


def count_nonspaces(string):
    amount = len(string)
    
    for i in string:
        if i == ' ':
            amount = amount - 1
        
    return amount


# In[2]:


count_nonspaces("I love you.")


# In[3]:


def count_spaces(string):
    amount = 0
    
    for i in string:
        if i == ' ':
            amount = amount + 1
        
    return amount


# In[4]:


def count_nonspaces_calling(string):
    return len(string) - count_spaces(string)


# In[5]:


count_nonspaces_calling("I love you.")

