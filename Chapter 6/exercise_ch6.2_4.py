
# coding: utf-8

# In[4]:


def initials(name):
    capital = ''
    
    for i in range(len(name)):
        if i == 0:
            capital = capital + name[0]
        elif name[i] == ' ':
            capital = capital + name[i+1]
        else:
            capital = capital
    
    return capital


# In[5]:


initials('International Business Machines')


# In[6]:


initials('Vladimir "Pootie-Poot" Putin')


# In[7]:


initials('Georges Perec')


# In[5]:


def initials_2(name):
    list = name.split(" ")
    capital = ''
    
    for i in range(len(list)):
        capital = capital + str(list[i])[0]
        
    return capital


# In[6]:


initials_2('Georges Perec')


# In[67]:


def initials_3(name):
    list_old = name.split(" ")
    
    
    for i in range(len(list_old)):
        list_new = []
        list_new.append(str(list_old[i])[0])
    
    return "".join(list_new)

## list_new가 반복문 안에 있을 경우 리셋됨.


# In[68]:


initials_3('International Business Machines')


# In[61]:


def initials_3(name):
    list_old = name.split(" ")
    list_new = []
    
    for i in range(len(list_old)):    
        list_new.append(str(list_old[i])[0])
    
    return "".join(list_new)


# In[66]:


initials_3('International Business Machines')


# In[64]:


initials_3('Vladimir "Pootie-Poot" Putin')


# In[65]:


initials_3('Georges Perec')

