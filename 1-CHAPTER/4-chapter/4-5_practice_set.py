a = (1, 7, 2)
#count(1) – It will return the number of times 1 occurs in a.
'''print(a.count(1))
print(a.index(1))
'''

# 1-Write a program to store seven fruits in a list entered by the user.
'''t1 = input("enter the 1st fruit name:")
t2 = input("enter the 2nd fruit name:")
t3 = input("enter the 3rd fruit name:")
t4 = input("enter the 4th fruit name:")
t5 = input("enter the 5th fruit name:")
t6 = input("enter the 6th fruit name:")
t7 = input("enter the 7th fruit name:")
List = [t1,t2,t3,t4,t5,t6,t7]
print(List)
'''
# 2-Write a program to accept the marks of 6 students and display them in a sorted manner.
'''s1 = int(input("enter the  student marks : "))
s2 = int(input("enter the  student marks : "))
s3 = int(input("enter the  student marks : "))
s4= int(input("enter the  student marks : "))
s5 = int(input("enter the  student marks : "))
s6 = int(input("enter the  student marks : "))
s7 = [s1,s2,s3,s4,s5,s5,s6]
print(s7)
s7.sort()
print("marks in sorted form are :", s7)
'''
# 3-Check that a tuple cannot be changed in Python.
'''t1 = (1,7,19,22)
print(t1[0])
print(t1[1])
print(t1[2])'''
'''t1[1] = 7
print(t1) tuple value can't be change. '''


# 4-Write a program to sum a list with 4 numbers.
'''a = [1,2,3,4]
b = [5,4,7,9]
c = a + b
print(c) #this will just join a and b.
d = a[0]+a[1]+a[2]+a[3]
print(d)
e = sum(a)
print(e)
f=sum(b)
print(f)
'''

# 5-Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
