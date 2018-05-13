
# coding: utf-8

# In[2]:


from PIL import Image


# In[8]:


def flop(pngimage):
    length = pngimage.size[1]
    
    if length % 2 == 0:
        length_half = length // 2
    else:
        length_half = (length - 1) // 2
        
    
    for x in range(pngimage.size[0]):
        for y in range(length_half):
            down = pngimage.getpixel((x, y))
            up = pngimage.getpixel((x, length - y - 1))
            pngimage.putpixel((x, length - y - 1), down)
            pngimage.putpixel((x, y), up)


# In[9]:


testimage = Image.open('flipme.png')
flop(testimage)
testimage.save('flopped.png')

