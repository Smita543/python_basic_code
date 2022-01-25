'''#1 Write a program to create a dictionary of Hindi words with values as their English translation. 
Provide the user with an option to look it up!  ''' 
dict = {"hindi":"english","A":"a","B":"b","C":"c"}
print(dict.items())
print(dict.keys())
print(dict.values())

#2 Write a program to input eight numbers from the user and display all the unique numbers (once).
n1 = int(input("enter the number "))
n2 = int(input("enter the number "))
n3 = int(input("enter the number "))
n4 = int(input("enter the number "))
n5 = int(input("enter the number "))
n6 = int(input("enter the number "))
n7 = int(input("enter the number "))
n8 = int(input("enter the number "))
number = {n1,n2,n3,n4,n5,n6,n7,n8}
print(number)

#3 Can we have a set with 18(int) and “18”(str) as a value in it?
number = {18,"18","smita","khushi"}
print(number) 

''' #4 What will be the length of the following set S:
What will be the length of S after the above operations? '''
'''S = set()
print(type(S))
S.add(20)
print(S)
S.add(20.0)
print(S)
S.add("20") 
print(S)
print(len(S))
'''

#5 S = {}, what is the type of S?
S = {}
print(type(S))

#6 Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names.
# Assume that the names are unique.
NAME = {"antina":"hindi","smita":"korean","harshit":"sanskrit","shivi":"english"}
print(NAME)

#7 If the names of 2 friends are the same; what will happen to the program in Program 6?
NAME = {"antina":"hindi","antina":"korean","harshit":"sanskrit","shivi":"english"}
print(NAME)

#8 If the languages of two friends are the same; what will happen to the program in Program 6?
NAME = {"antina":"hindi","smita":"korean","harshit":"english","shivi":"english"}
print(NAME)

''' #9 Can you change the values inside a list which is contained in set S '''
S = {8, 7, 12,"Harry", [1, 2]} # unhashable type: 'list' , will throw error if list is defined under set.

# print(type(S))