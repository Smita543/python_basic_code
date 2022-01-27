import numpy
# a = numpy.array([1,2,34])
# print(a)

from numpy import *
# b = array([1,2,3,4])
# print(b)

a = array([1,2,3,4,5])
for i in range(len(a)):
    a[i] = 5 +a[i]
    print(a[i],end=" ")
    i+=1

# a = a + 5
# print(a)