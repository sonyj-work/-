
# coding: utf-8

# In[1]:


def devowel(string):
    for c in string:
        if c in [a, e, i, o, u]:
            string = string - c
    
    return string


# In[2]:


devowel('hello world')


# In[3]:


def devowel(string):
    for c in string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            string = string - c
    
    return string


# In[4]:


devowel("I love you.")


# In[6]:


def devowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(string)+1):
        if string[i] in vowel:
            string[i] = ''
    
    return string


# In[7]:


devowel("I love you.")


# In[8]:


def devowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_new = ''
    
    for i in range(len(string)+1):
        if string[i] in vowel:
            string_new[i] = ''
        else:
            string_new[i] = string[i]
    
    return string_new


# In[9]:


devowel("I love you.")


# In[10]:


def devowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_new = ''
    
    for i in range(len(string)+1):
        if string[i] in vowel:
            string_new[i] = ''
            i = i - 1
        else:
            string_new[i] = string[i]
    
    return string_new


# In[11]:


devowel("I love you.")


# In[29]:


def devowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_new = ''
    
    for i in range(len(string)):
        if string[i] in vowel:
            string_new += string[:i]
        else:
            string_new += string[:i+1]
    
    return string_new

## In Python, strings are not mutable, which means they cannot be changed.
## You can, however, replace the whole variable with the new version of the string.


# In[30]:


devowel ("I love you")


# In[31]:


def devowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_new = ''
    
    for i in range(len(string)):
        if string[i] not in vowel:
            string_new = string_new + string[i:i+1]
        else:
            string_new = string_new

    return string_new


# In[32]:


devowel ("I love you")


# In[33]:


devowel ("I love yours.")

