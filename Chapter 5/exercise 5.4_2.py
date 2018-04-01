
# coding: utf-8

# In[5]:


def division():
    answer = 'Error occured during calcuating.'
    if num % 2 == 1:
        answer = 'It is odd number.'
    elif num % 2 == 0:
        answer = 'It is even number.'
    else:
        print 'Error'

    return answer


# In[3]:


division(100)


# In[7]:


division(-10)


# In[8]:


division(a)


# In[37]:


def division(num):
    indicated = '?'
    if num % 2 == 1:
        indicated = 'It is an odd number.'
    elif num % 2 == 0:
        indicated = 'It is an even number.'

    return indicated


# In[38]:


division(3)


# In[36]:


division('a')

