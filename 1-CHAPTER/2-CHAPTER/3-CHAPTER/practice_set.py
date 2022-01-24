#1 Write a Python program to display a user-entered name followed by Good Afternoon using input() function
'''a = input("enter the name: ")
b = print("good afternoon",a)
b = print("good afternoon, " + a)
'''
# ................................................../////////////////////////////////............................

#2 Write a program to fill in a letter template given below with name and date.
# letter =''' Dear <|NAME|>,
# happy to announce you that you have been selected.
# you are a good and i would say the best coder of all time.
# so, glad that you are selected in our firm .you are the best choice of firm.

# You are selected!
# thanks for your time !!

# <|DATE|>'''
# THIS BELOW CODE IS NOT THE EFFICIENT WAY TO WRITE A CODE :
# print(letter.replace("<|NAME|>", "SMITA"))
# print(letter.replace("<|DATE|>", "25,AUG" ))

#---------------------efficient code to write------------------
# name = input("ENTER THE NAME\n")
# date = input("enter the date\n")

# letter = letter.replace("<|NAME|>",name)
# letter = letter.replace("<|DATE|>",date)

# print(letter)
# .............................................................///////////////////////////............................

#3 Write a program to detect double spaces in a string.
phase = "hello guys  happy"
print(phase.find("  "))