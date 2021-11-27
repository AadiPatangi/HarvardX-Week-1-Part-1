import numpy as np
import math
import random
x = np.array([1,3,5])
y = np.array([1,5,9])
print(x.mean())   #since there is double parenthesis around mean, it is a function
print(y.mean())
print(x.shape)   #since there is no double parenthesis around shape, it means that it is a data attribute
print(y.shape)   #returns amount of values in the array

print(math.pi)
print(math.sqrt(8))
print(math.sqrt(9))

x2 = np.array([x,y])

print(x2.shape) #in 2d array, it returns length, width

print(math.sin(math.pi/2))
print(np.sqrt([4,9,12])) #not possible using math.sqrt

name = "qwerty"
print(type(name))
print(dir(name))
print(help(name.upper))


print(12/8)  #flotating point division  (returns exact number which can include decimals)
print(12//8) # returns whole number  which is rounded version of floating point number
print(math.factorial(4))
print(12**8)   #12 to the eighth power
list1 = [2,45,3,787]
print(random.choice(list1)) #prints random value from list1

#boolean
print(type(True))
print(True or False)   # or returns True if one or the other is true
print(True and True)  # and returns True if both objects are true
print(not True)  #returns the opposite boolean value
print(2<= 4)
print(2.0 == 2) #returns true even if one is a floating point number and the other is integer
