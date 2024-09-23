#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytube3


# In[2]:


pip install --upgrade pytube


# In[3]:


from pytube import YouTube


# In[5]:


pip install yt-dlp 


# In[13]:


link = input("Enter youtube vedio")
yt = YouTube(link)


# In[14]:


#TO print title
print("Title :", yt.title)
#To get number of views
print("Views :", yt.views)
#To get length of vedio
print("Duration", yt.length)
#To get description
print("Description :", yt.description)
# To get ratings
print("Ratings :", yt.rating)


# In[15]:


from yt_dlp import YoutubeDL


# In[17]:


download_option = input("Do you want to download this vedio? (yes/no): ").lower()
if download_option == "yes" :
    url = 'https://www.youtube.com/watch?v=lgHQ-u765HA'
    ydl_opts = {'format' : 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        print("DOwnloading....")
        ydl.download([url])
        print("Download completed.")
else :
    print("Download aborted")


# In[18]:


import os
os.getcwd()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




