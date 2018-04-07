
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

