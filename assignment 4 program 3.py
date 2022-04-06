#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to square the elements of a list using map() function.

# In[3]:


def square(n):
    return n*n
x=[4,5,2,9]
sqr=map(square,x)
print("square the elements of the list:")
print(list(sqr))


# In[ ]:




