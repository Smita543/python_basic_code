#1 wap to print to print all values from 1 to 100:
for i in range (101):
    print(i)

#2 wap to skip no. which are divisible by 3 or 5:

for i in range (100):
    if i%3 == 0 or i%5 == 0 :
        continue
    print(i)
    i+=1

# using while loop 2 => wap to skip no. which are divisible by 3 or 5:
# i = 1
# while i <100:
#     while i%3 !=0 or i%5 !=0 :
#         print(i)
#         i+=1