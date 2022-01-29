# from array import *
# arr = array('i',[ ])
# n = int(input ("enter the length of number"))
# for i in range(n):
#     x = int(input("enter the no."))
#     arr.append(x)
#
# print(arr)

from array import *
a = array('i',[])
b = int(input("enter the length "))
for i in range(b):
    c = int(input("enter the name "))
    a.append(c)

print(a)

# //===================array item must be unicode character (error is coming)===================

# from array import *
# a = array('u',[" "])
# b = int(input("enter the length"))
# for i in range(b):
#     c = str(input("enter the name "))
#     a.append(c)

# print(a)

val = int(input("enter the number to find in a "))
#====== using loop to find index =============
k = 0
for i in a:
    if val== i:
        print(k)
        break
    k+=1

#  =======  directly using module to print the value =======
print(a.index(val))