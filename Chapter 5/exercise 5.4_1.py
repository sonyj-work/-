
# coding: utf-8

# In[1]:


class YearsChanger(object):
    def __init__ (self, value, scale):
        if scale.lower() == 'd':
            self._dogyears = float(value)
        elif scale.lower() == 'h':
            self._dogyears = value * 7
        
    
    def d(self):
        return str(self._dogyears) + ' year(s) old.'
    def h(self):
        return str(self._dogyears * 7) + ' year(s) old.'


# In[2]:


Kameron = YearsChanger(25, d)
Kameron.h()


# In[3]:


class YearsChanger(object):
    def __init__ (self, value):
        self._dogyears = float(value)
        
    
    def d(self):
        return str(self._dogyears) + ' year(s) old.'
    def h(self):
        return str(self._dogyears * 7) + ' year(s) old.'


# In[4]:


Kameron = YearsChanger(100)


# In[5]:


Kameron.h()


# In[6]:


Kameron.d()


# In[8]:


class AgeChanger(object):
    def __init__ (self, value):
        self._dogyears = float(value)
        self._humanyears = float(value)
    
    def d(self):
        return str(self._humanyears / 7) + ' year(s) old in human age.'
    def h(self):
        return str(self._dogyears * 7) + ' year(s) old as in dog age.'


# In[9]:


Kameron = AgeChanger(100)


# In[10]:


Kameron.d()


# In[11]:


class AgeChanger(object):
    def __init__ (self, value):
        self._dogyears = float(value)
        self._humanyears = float(value)
    
    def d(self):
        return str(self._humanyears / 7) + ' year(s) old in a dog age.'
    def h(self):
        return str(self._dogyears * 7) + ' year(s) old as in a human age.'


# In[17]:


class Age(object):
    def __init__ (self, value, scale):
        if scale.lower() == 'd':
            self._years = float(value)
        elif scale.lower() == 'h':
            self._years = value * 7
    
    def d(self):
        return str(self._years * 7) + ' year(s) old in human age.'
    def h(self):
        return str(self._years / 49) + ' year(s) old as in dog age.'


# In[19]:


Kameron = Age(100, 'h')
Kameron.d()


# In[21]:


Kameron = Age(100, 'd')
Kameron.d()


# In[22]:


Kameron.h()


# In[23]:


class Age(object):
    def __init__ (self, value, scale):
        if scale.lower() == 'd':
            self._years = float(value)
        elif scale.lower() == 'h':
            self._years = value / 7
    
    def d(self):
        return str(self._years) + ' year(s) old in dog age.'
    def h(self):
        return str(self._years * 7) + ' year(s) old as in human age.'


# In[25]:


Karl = Age(100, 'h')
Karl.d()


# In[26]:


Karl = Age(100, 'h')
Karl.h()


# In[27]:


Karl = Age(2.5, 'd')
Karl.h()


# In[28]:


Karl = Age(2.5, 'h')
Karl.d()


# In[29]:


Karl = Age(2.5, 'd')
Karl.d()

