#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="  Hello world  "
b="lokesh"

print(len(a)) #just count, does not return 
print(a+b)
print(a,b)
print('@'.join(a)) #add @ in between each alphabet
print(a.upper()) #it will return value 
print(a.lower())
print(a.strip()) # remove excessive space
print(a.replace('world','there')) 


# In[13]:


a="MATHEMATICS"
print(a[-1])
print(a[0])
print(a[1])
print(a[0:4]) #will print 0,1,2,3 th index value
print(a[0:]) #will take completely
print(a[:11]) #it will also take completely because 11 is the size of the word
print(a[1:6:2])


# In[51]:


a=input("Enter the data:")
b=len(a)
for i in range(b):
    c=int(a[i])
    d=c*c*c
    #print(d)
    for j in range(b):
        am=d
print(am)
    
    
 


# In[61]:


a=input("Enter your string:")       
b=int(input("Enter no of characters:"))
print(f"\nFirst {b} characters are: {a[ :b]}")
print(f"Last {b} characters are: {a[-b:]}")
print(f"Reverse of the string is: {a[ : :-1]}")


# In[96]:


# list
# A collection of multiple data types in order, mutable and allow duplicate value

a= [1,1.2,"Apple",True]

print(a)
print(a[2])

a.append(5) # add 5 to the list at the end
print(a)

a.extend([6,7,8]) # add 6,7,8 to the list at the end 
print(a)

a.insert(2,8) # add 8 in the index of 2
print(a)

a.remove(1) # remove the value 1
print(a)

a.pop() # remove the last value in the list
print(a)
a.pop(1) # remove the value in the index 1
print(a)

print(a.index(5)) # return the index value of 5

a=[1,2,2,2,2,2,2,3,4] # return the no of time the value 2 occur in the list
print(a.count(2))

a=[7,4,8,5,1,0] # sort in asscending order
a.sort()
print(a)

a=[7,4,8,5,1,0]
a.reverse() #return from the last
print(a)
a.sort(reverse=True) #sort in descending order 
print(a)

b=a.copy() # copying the list to other 
print(b)

a.clear() # removing entire value form the list
print(a)

a=[7,4,8,5,1,0]
print(len(a)) # return the size of the list
print(max(a))
print(min(a))
print(sum(a))


# In[96]:


# list
# A collection of multiple data types in order, mutable and allow duplicate value

a= [1,1.2,"Apple",True]

print(a)
print(a[2])

a.append(5) # add 5 to the list at the end
print(a)

a.extend([6,7,8]) # add 6,7,8 to the list at the end 
print(a)

a.insert(2,8) # add 8 in the index of 2
print(a)

a.remove(1) # remove the value 1
print(a)

a.pop() # remove the last value in the list
print(a)
a.pop(1) # remove the value in the index 1
print(a)

print(a.index(5)) # return the index value of 5

a=[1,2,2,2,2,2,2,3,4] # return the no of time the value 2 occur in the list
print(a.count(2))

a=[7,4,8,5,1,0] # sort in asscending order
a.sort()
print(a)

a=[7,4,8,5,1,0]
a.reverse() #return from the last
print(a)
a.sort(reverse=True) #sort in descending order 
print(a)

b=a.copy() # copying the list to other 
print(b)

a.clear() # removing entire value form the list
print(a)

a=[7,4,8,5,1,0]
print(len(a)) # return the size of the list
print(max(a))
print(min(a))
print(sum(a))


# In[131]:


a=[1,1.2,"lokesh",True]
print(a[2])


# In[161]:


a=int(input("Enter your size of the list:"))
for i in range(1,a+1):
    z=input(f"Enter your data for {i}:"))
    for j in range (0,a+1):
        x[j]=list(z)
        break
    print(x, end='')


# In[109]:


a=[1,1.2,"lokesh",True]
b=input("Enter an item to append a list:")
a.append(b)
print(a)


# In[119]:


a=[1,1.2,"lokesh",True]
a.remove(1)
print(a)
a=a
a.pop()
print(a)
a.clear()
print(a)


# In[147]:


# LIST - ordered,mutable, allow duplicate,[square braces],dynamic, slower
# TUPLE - ordered,immutable, allow duplicate,(parenthesis),faster, Safety, Better performance (because it is static memory)


# In[153]:


a=(1,1.2, 4,5,6)
print(a[3])


# In[149]:


a=(1,1.2,1,5,6)
print(a.count(1))


# In[151]:


a=(1,1.2,4,5,6)
print(a.index(5))


# In[ ]:


# SETS - unordered,immutable, don't allow duplicate,{curly braces} 
# DICTIONARIES - ordered,mutable, don't allow duplicate


# In[222]:


a={1,1.2,4,0}
print(a)
a={1,1,1.2,4,0} # don't allow duplicate
print(a)
a={True,1,4,0} # true will be taken as 1 and 1 after true will be considered as duplicate of it and don't allow/print it 
print(a) # false as 0 and the same principle of true applies 

a={1,2,3,4,5,6}
b={1,8,9,0} # union and update exclude duplicate
#c=a.union(b)
print(a.union(b))

c=a|b # similar to union
print(c)

c=a.intersection(b) # print value which is in both set
print(c)

c=a&b # similar to intersection 
print(c)


# In[221]:


a={
    "name":"ghost",
    "age":20,
    "course":"AI"
    }

print(a)
print(a["name"]) # access the value under name
x=a.get("age") # access the value by using get 
print(x)

x=a.keys() # return list of all keys
print(x)

x=a.values() # return list of all values
print(x)

x=a.items() #return both keys and values as tuples in a list
print(x)

a["Qualification"] = "B.E - C.S.E" # add a new key value pair 
print(a)

a.update({"age": 21}) # update pre-existing pair value if it exit
a.update({"Days": 100}) # if not it will add as a new key value pair
print(a)

a.pop("Days") # remove days key value pair from the dictionary
print(a)
a.popitem() # remove the last key value pair form the dictionary
print(a)

del a["course"]
print(a)

#a.clear()
#print(a)

del a
print(a)


# In[239]:


# create a function to add numbers
# check odd or even
# default parameter

def add():
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    print(num1+num2)
    
add()

def ore(x):
    if (x%2==0):
        print("EVEN")
    else:
        print("ODD")
x=int(input("Enter your data:"))
ore(x)

def para(de = "Parameter"):
    print(de)
para()


# In[7]:


# handle division by zero
# invalid  input
# keyerror in dictionary

try:
    a=int(input("Enter your data:"))
    b=a/0
except ZeroDivisionError:
    print("Zero Division Zero")

try:
    a=int(input("Enter your data:"))
except ValueError:
    print("Value Error")
else:
    print(f"Given value is an integer")
finally:
    print("Value error is finished")

try:
    dic1={
        "name":"Ghost",
        "age":23,
    }
    print(dic1["place"])
except KeyError:
    print("Key Error")
    



# In[57]:


# Numpy
import numpy as np
a=np.array([1,2,3]) # 
print(a.ndim) # check its type (array)
print(a) 
print(a.shape) # meaning 3 elements in a single dimension (1D array).
print(type(a)) 



# In[59]:


b=np.array([[1,2],[3,4]]) # 2d array
print(b) 
print(b.shape) 


# In[61]:


c=np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2d array 
print(c.ndim)
print(c[1])
print(c[1,2]) 
print(c.shape)


# In[41]:


d=np.ones([2,2]) 
print(d) # give 2x2 matrix with values of 1 in float

e=np.zeros([2,2]) 
print(e) # give 2x2 matrix with values of 0 in float


# In[35]:


f=np.random.random([2,2]) # module,function (print values between 0-1 in float)
print(e)


# In[56]:


# array math 
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print(c) # normal math operation
print(np.add(a,b)) 
d=a-b
print(d)
print(np.subtract(a,b))
e=a*b
print(e)
print(np.multiply(a,b))
f=a/b
print(f)
print(np.divide(a,b))


# In[78]:


# array concat
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.concatenate((a1,a2))) # note np.concatenate((a,b))

a3=np.array([[1,2,3],[4,5,6]])
a4=np.array([[40,40,40],[50,40,40]])
print(np.concatenate((a3,a4),axis=0))
print(np.concatenate((a3,a4),axis=1))
print(np.concatenate((a3,a4),axis=0))


# In[83]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.stack((a1,a2)))


# In[82]:


a3=np.array([[1,2,3],[4,5,6]])
a4=np.array([[40,40,40],[50,50,50]])
print(np.stack((a3,a4)))
print(np.hstack((a3,a4)))
print(np.vstack((a3,a4)))
print(np.dstack((a3,a4)))


# In[93]:


# array reshape
a = np.array([[1,1,1],[2,2,2]])
print(a)

b = np.reshape(a,(3,2))
print(b)

# ravel return a view doesn't create a copy but refers to original array 
# flatten return the completey new copy of the array 

c=np.array([[1,1],[2,2]])
d=np.ravel(c)
print("Original Array: ",c)
print("Flattened using Ravel: ",d)
d[0]=99
print("After modifying d")
print("Original array:",c) # original value get affected(updated) here
print("Modified d:",d)

c=np.array([[1,1],[2,2]])
d=c.flatten()
print("Original Array: ",c)
print("Flattened using Ravel: ",d)
d[0]=99
print("After modifying d")
print("Original array:",c) # original value don't get affected 
print("Modified d:",d)


# In[ ]:


Task 1: Creating and modifying an array
Task 2 : Finding min, max, and mean
Task 3 : Reshaping and flattening an array
Task 4 : Create two 2×2 arrays and stack them vertically & horizontally
Task 5 : Convert a 1D array of size 9 into a 3×3 matrix
Task 6 : Create an array from 1 to 10 and reverse it


# In[144]:


import numpy as np

# Creating and modifying an array
print("\n")
arr1=np.array([1,2,3,4,5,6])
print(f"Before modifying an array:",arr1)
arr1[5]=10
print(f"After modifying an array:",arr1)

# Finding min, max, and mean
print("\n")
arr1=[1,2,3]
arr2=[4,5,6]

print(f"Minimum:",np.min(arr1+arr2))
print(f"Maximum:",np.max(arr1+arr2))
print(f"Mean:",np.mean(arr1+arr2))

# Reshaping and flattening an array
print("\n")
arr1=np.array([[1,2],[3,4]])
a=arr1.flatten()
print(f"Flatten:\n",a)
b=np.reshape(a,(2,2))
print(f"Reshape:\n",b)

# Create two 2×2 arrays and stack them vertically & horizontally
print("\n")
arr1=np.array([[1,2],[3,4]])
v=np.vstack((arr1))
print(f"vertical:\n",v)
h=np.hstack((arr1))
print(f"Horizontal:\n",h)

# Convert a 1D array of size 9 into a 3×3 matrix 
print("\n")
arr1=np.array([1,2,3,4,5,6,7,8,9])
a=np.reshape(arr1,(3,3))
print(f"3x3 matrix:\n",a)

# Create an array from 1 to 10 and reverse it
print("\n")
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr=arr1[::-1]
print(f"Reverse:\n",arr)


# In[ ]:





# In[ ]:




