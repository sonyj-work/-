
# coding: utf-8

# In[3]:


def same_last(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    
    for i in string1, string2:
        if string1[-1:] == string2[-1:]:
            return True
        else:
            return False


# In[5]:


same_last('I love you', 'Ai Shiteru')


# In[1]:


def same_last(string1, string2):
    return string1[-1:] == string2[-1:]


# In[2]:


same_last('I love you', 'Ai Shiteru')

