#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 2.	(6 pts) Create a function that solves the zeros of a quadratic 
# equation (note that there are 3 possible outcomes, when finding the real
# zeros of a quadratic equation so your function must be able to handle 
# all 3, properly).  
import math

def quadratic(a, b, c):
    if b**2 - 4*a*c < 0 :
        zero_1 = str((-b)/(2*a)) + " + " + str(math.sqrt(abs(b**2 - 4*a*c))/(2*a)) + "i"
        zero_2 = str((-b)/(2*a)) + " - " + str(math.sqrt(abs(b**2 - 4*a*c))/(2*a)) + "i"
    else :
        zero_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        zero_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    zeros = (zero_1, zero_2)
    return zeros

# Test your function on: 
# a.	2x^2 + 3x + 1
q2a = quadratic(2, 3, 1)
print("The zeros of 2x^2 + 3x + 1 are %s" % (q2a,))

# b.	2x^2 - 2
q2b = quadratic(2, 0, -2)
print("The zeros of 2x^2 - 2 are %s" % (q2b,))

# c.	x^2 + 4
q2c = quadratic(1, 0, 4)
print("The zeros of x^2 + 4 are %s" % (q2c,))


# In[16]:


import numpy as np

mA = [1, 2, -4, 3, 0, -1, -2, 4]
mb = [3, 2, -1, 1, -2, 0]
A = np.array(mA).reshape(-1,2)
b = np.array(mb).reshape(2,-1)

print(A)
print()
print(b)
print()

np.matmul(A,b)


# In[ ]:




