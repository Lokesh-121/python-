#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("Enter your data for a:"))
b=int(input("Enter your data for b:"))

c=int(input("Enter your operation 1.Sum 2.Dif 3.Mul 4.Div"))
if(c==0):
    print("Invalid operation preferred\n Pls choose between 1-4")
    c=int(input("Enter your operation 1.Sum 2.Dif 3.Mul 4.Div"))
elif(c<=4):
    print("Your operation result is :")
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    print(a//b)
else:
    print("Invalid operation")


# In[ ]:





# In[2]:


print("<Average>")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

e=a/2


d=a+b+c
ans=d//3

print("Average of your given numbers is: ",ans)


# In[3]:


print("<For loop>")
a=int(input("Enter your data for a:"))
b=int(input("Enter your data for b:"))
c=int(input("Enter your data for c:"))

arr=[a,b,c]

for x in arr:
    print(x,'')
    x+=1


# print("<while loop>")
# a=int(input("Enter your data for a:"))
# b=int(input("Enter your data for b:"))
# c=int(input("Enter your data for c:"))
# 
# arr=[a,b,c]
# 
# for x in arr:
#     print(x,'')
#     x+=1

# In[5]:


n=11
for i in range(1,n):
    print(i)


# In[6]:


print("<ODD | EVEN>")
a=int(input("Enter your data for a:"))

if a%2==0:#n%2==0
    print(a," is an EVEN number")
else:
    print(a,"is an ODD number")


# In[7]:


print("<LARGEST>")
a=int(input("Enter your data for a:"))
b=int(input("Enter your data for b:"))

if b>a:
    print(b, "is the LARGEST")
else:
    print(a, "is the LARGEST")


# In[8]:


print("<GRADING>")
x=int(input("Enter your data for a:"))
#b=int(input("Enter your data for b:"))

if x>90: 
    print(x," achieve A+ grade")
elif x>80:
    print(x," achieve A grade")
elif x>50:
    print(x," achieve B grade")
elif x>=35:
    print(x," achieve C grade")
else:
    print("Failed")



# In[9]:


print("< POSITIVE | NEGATIVE >")
a=int(input("Enter your data for a:"))

if a>0:
    print(a," is an POS number")
elif a==0:
    print(a," =0")    
else:
    print(a,"is an neg number")


# In[10]:


print("< LARGEST OF 3 NUMBERS >")
a=int(input("Enter your data for a:"))
b=int(input("Enter your data for b:"))
c=int(input("Enter your data for c:"))

if a>b and a>c:
    print(a," is LARGEST number")
elif b>a and b>c:
    print(b," is LARGEST number")    
else:
    print(c,"is LARGEST number")


# In[11]:


print("< LEAP YEAR>")
a=int(input("Enter your data for a:"))

if a%4==0:
    print(a," is LEAP year")
else:
    print(a,"is not a LEAP year")


# In[12]:


print("< AEIOU >\n")

a=input("Enter your data:")

vowel ='aeiouAEIOU'

if a in vowel:
    print(a," is VOWEL")
    #a+=1
else:
    print(a,"is CONSONENT")


# In[13]:


print("< SIMPLE CALCULATOR >\n")

a=int(input("Enter your data for a:"))
b=int(input("Enter your data for b:"))

o=int(input("Enter your choice 1.SUM 2.DIF 3.MUL 4.DIV"))

if o==1:
    print("SUM:",a+b)
elif o==2:
    print("DIF:",a-b)
elif o==3:
    print("MUL:",a*b)
elif o==4:
    print("DIV:",a//b)
else:
    print("Invalid operation")


# In[14]:


a=int(input("enter the number:"))
if a % 2==0:
    print(a, "is a even number")
else:
    print(a,"is odd number")


# In[15]:


a=int(input("enter the data a:"))
b=int(input("enter the data b:"))
if a > b:
    print(a,"is greater than b")
else:    
    print(b,"is smaller than a")


# In[16]:


print("<PRIME NUMBER>\n")


for num in range(2, 101):  # Start from 2 since 0 and 1 are not prime
   # is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


'''
for n in range(0,101,1):
    if n==0:
        print(n," is Neither PRIME nor COMPOSITE number")
    else:
        for d in range(2,100,1):
            if n%d==0: 
                print(n," is a COMPOSITE number")
            else:pass
    print(n," is a PRIME number")
    '''
    


# print("<FACTORIAL>\n")
# 
# n = int(input("Enter a non-negative integer: "))
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     print("The factorial of",n,"is",f)
# 
# 
#     
# 

# In[18]:


print("<TABLES>\n")

t=int(input("Enter your data:"))

for i in range(1,11,1):
    print(i,"*",t,"=",i*t)


# In[ ]:


print("<FIBBO SERIES>\n")
'''
#a=int(input("Enter your number 1:"))
#b=int(input("Enter your number 2:"))
a=0
b=1
c=int(input("Enter non-negative number:"))
if c>0:
    

    print(a)
    print(b)
    or i in range(,c,1):
        i=b+a
        print(i)else:
    print("Invalid data")
    '''

a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b


# In[ ]:





# In[ ]:


print("<EVEN NUMBERS using FOR LOOP>\n")

for i in range(1,51):
    if i%2==0: print(i)
print(" are an even number")


# In[ ]:


print("<EVEN NUMBERS using FOR LOOP>\n")

for i in range(1,51):
    if i%2==0:
        print( i, end='')
print(" are an even number")



# In[ ]:


for i in range(1,51,2):
    print("Even Numbers are:",i)


# In[ ]:





# In[ ]:


# Program to find factorial using for loop

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
    for i in range(2, num + 1):  # Loop from 2 to num
        factorial *= i
    print(f"The factorial of {num} is {factorial}")


# In[ ]:


i=10

if i<=10:
    print(1)
else:
    pass


# In[27]:


print("<Factorial>\n")

a=int(input("Enter your data:"))
factorial=1
for i in range(2,a+1):
    factorial*=i
print(factorial)


# In[26]:


# Program to find factorial using for loop

num = int(input("Enter a number: "))
factorial = 1
'''
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
'''
for i in range(2, num + 1):  # Loop from 2 to num
    factorial *= i
print(f"The factorial of {num} is {factorial}")


# In[ ]:





# In[ ]:




