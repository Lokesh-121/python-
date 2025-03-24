#!/usr/bin/env python
# coding: utf-8

# In[22]:


print("<SWAPPING using TEMP>\n")
a=int(input("Enter your data:"))
b=int(input("Enter your second data:"))

print("Before swap a and b:",a,b)
c=a
a=b
b=c
print("After swap a and b:",a,b)


# In[21]:


print("<SWAPPING without using TEMP>\n")
a=int(input("Enter your data:"))
b=int(input("Enter your second data:"))

array=[a,b]
print("Before swap a and b:",array)

for i in array:
    a=array[1]
    b=array[0]
array=[a,b]
print("After swap a and b:",array)


# In[23]:


a,b = 2,3
print("before swapping:",a,"and",b)
a,b = b,a
print("after swapping:",a,"and",b)


# In[54]:


print("<FACTORIAL>\n")

a=int(input("Enter your data:"))

if a==0 or a==1:
    print("Factorial of ",a,"is : 1")
else:
    for i in range(a,0):
        
        print(i*i-1)


# In[ ]:




