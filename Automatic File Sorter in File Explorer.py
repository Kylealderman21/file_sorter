#!/usr/bin/env python
# coding: utf-8

# # Automate File Sorter

# In[34]:


import os, shutil


# In[35]:


path = r"C:/Users/kalde/Desktop/Python Project/"


# In[41]:


file_names = os.listdir(path)


# In[39]:


folder_names = ['excel files', 'image files', 'text files', 'word docs']

#loop through folder_names, if folder names do not exist in the path, create the folders in the loop

for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))


# In[38]:


#if files are in file_names and not in the new folders, then move the corresponding files to the folders.

for file in file_names:
    if ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file,path + "text files/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "excel files/" + file):
        shutil.move(path + file,path + "excel files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file,path + "image files/" + file)
    elif ".docx" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file,path + "word docs/" + file)

