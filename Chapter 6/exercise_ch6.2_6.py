
# coding: utf-8

# In[1]:


def tautonym(string):
    return string[:len(string)/2] == string[len(string)/2:]


# In[2]:


tautonym("I love you")


# In[3]:


def tautonym(string):
    return string[:int(len(string))/2] == string[int(len(string))/2:]


# In[4]:


tautonym("I love you.")


# In[6]:


def tautonym(string):
    length = len(string)
    
    if length % 2 == 1:
        return false
    else:
        return string[:length/2] == string[length/2:]


# In[7]:


tautonym("worldworld")


# In[25]:


def tautonym(string):
    length = len(string)
    
    if length % 2 == 1:
        return False
    else:
        for i in range(len(string)):
            return string[i] == string[i+int(length/2)]

## how i solved the error
https://stackoverflow.com/questions/20733156/slice-indices-must-be-integers-or-none-or-have-index-method


# In[26]:


tautonym("worldworld")


# In[33]:


def tautonym(string):
    length = len(string)
    
    if length % 2 == 1:
        return False
    else:
        for i in range(len(string)):
            return string[i] == string[i+int(length/2)]


# In[34]:


tautonym("helloworld")

