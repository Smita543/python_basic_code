# import array as arr
# arr.array()

# from array import *
# vals = array("i",[5,6,9,-10])
# print(vals)

from array import *
vals = array("I",[5,6,9,10,10,9,4])
print(vals)

# print(vals.pop(2)) #pop removes the value from index
# print(vals)
print(vals.count(10))
print(vals.index(9))
print(vals.buffer_info())
vals.append(3)
print(vals)
vals.reverse()
print(vals)
print(max(vals))

# for i in range (1,5):
#     print(i)

print()
number = [1,2,6,9,11]
for i in range(len(number)):
    print(number[i])
print()

name = ["smita","sumit","shashank","sunita","smita"]
for i in range(len(name)):
    print(name[i])

print(name.count("smita"))
print(name.count("harsh"))
print(max(name))

for e in number:
    print(e)

char = array('u',["a","e","i","o","u"])
print(char)
for i in range(len(char)):
    print(char[i])