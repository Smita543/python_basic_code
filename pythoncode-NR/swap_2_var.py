a = 5
b = 6
# c = a+b
# print(a+b)
# using 3 variable
temp = a
a = b
b = temp
print(a)
print(b)
# without using 3 variable
a = a+b
b = a-b
a = a-b
print(a)
print(b)

# we can use logical operators also .
a = a^b
b = a^b
a = a^b
print(a)
print(b)

# rot-two variable
c = 10
d = 11
c,d = d,c
print(c)
print(d)