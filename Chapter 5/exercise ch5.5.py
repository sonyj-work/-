
# coding: utf-8

# In[12]:


def factorial(n):
    answer = 1
    for num in range(1, n):
        answer = answer * num
    return answer

def fact_calling(n):
    if n == 0:
        return 1
    elif n < 0:
        raise Exception('It cannot be calculated')
    else:
        return factorial(n)


# In[21]:


fact_calling(-3)


# In[18]:


fact_calling(30)


# In[16]:


def factorial(n):
    answer = 1
    for num in range(1, n+1):
        answer = answer * num
    return answer

def fact_calling(n):
    if n == 0:
        return 1
    elif n < 0:
        raise Exception('It cannot be calculated')
    else:
        return factorial(n)
    
print (fact_calling(5))


# In[20]:


fact_calling(3)

