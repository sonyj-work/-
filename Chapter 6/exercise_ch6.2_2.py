
# coding: utf-8

# In[1]:


def count_spaces(string):
    amount = 0
    
    for i in string:
        if i = ' ':
            amount = amount + 1
        
    return amount


# In[2]:


def count_spaces(string):
    amount = 0
    
    for i in string:
        if i == ' ':
            amount = amount + 1
        
    return amount


# In[3]:


count_spaces("I love you.")


# In[4]:


def count_spaces_2(string):
    return len(string.split()) -1

## 새로운 변수를 만들지 않을 수 있음. (단어와 문장의 관계 이용.)


# In[5]:


count_spaces_2("I love you.")


# In[8]:


def count_spaces_3(string):
    for i in string:
        if string[i] == ' ':
            print (sum(i))


# In[9]:


count_spaces_3("I love you.")


# In[10]:


def count_spaces_3(string):
    for i in range(len(string)):
        if string[i] == ' ':
            print (sum(i))


# In[11]:


count_spaces_3("I love you.")


# In[12]:


def count_spaces_3(string):
    for i in range(len(string)):
        if string[i] == ' ':
            print (sum(len(string[i]))


# In[13]:


def count_spaces_3(string):
    for i in range(len(string)):
        if string[i] == ' ':
            print (sum(len(string[i])))


# In[14]:


count_spaces_3("I love you")


# In[15]:


def count_spaces_4(string):
    for i in string:
        if string[i] == ' ':
            string_new[i] = string[i]
    
    return sum(string_new)


# In[13]:


count_spaces_4("I love you")


# In[17]:


def count_spaces_4(string):
    for i in range(len(string)+1):
        if string[i] == ' ':
            string_new[i] = string[i]
    
    return sum(string_new)


# In[18]:


count_spaces_4("I love you.")


# In[3]:


def count_spaces_4(string):
    string_new = []
    
    for i in range(len(string)):
        if string[i] == ' ':
            string_new = string_new + string[i]
    
    return sum(string_new)


# In[4]:


count_spaces_4("I love you.")


# In[14]:


def count_spaces_4(string):
    string_new = ''
    
    for i in range(len(string)):
        if string[i] == ' ':
            string_new = string_new + string[i]
        
    return len(string_new)

## string_new 라는 string을 새로 만들었음. string_new가 새로 생겼으므로 이에 대한 다른 함수를 생성하거나 이용가능.


# In[15]:


count_spaces_4("I love you.")


# In[25]:


def count_spaces_3(string):
    repository = []
    
    for i in range(len(string)):
        if string[i] == ' ':
            repository.append(string[i])
    
    return len(repository)


## https://wikidocs.net/14#append
## repository라는 리스트를 새로 만들어서, 그 속의 요소의 개수를 세는 함수.
## repository가 새로 생겼으므로 이에 대한 다른 함수를 생성하거나 이용가능.


# In[26]:


count_spaces_3("I love you.")


# In[27]:


def count_spaces_3_2(string):
    repository = []
    
    for i in range(len(string)):
        if string[i] == ' ':
            repository.append(len(string[i]))
    
    return sum(repository)

## repository라는 리스트에, 요소로 공백 하나 들어가는 것이 아님.
## 공백 하나에 len(string[i]) == 1 의 값을 부여한 셈.


# In[28]:


count_spaces_3_2("I love you.")

