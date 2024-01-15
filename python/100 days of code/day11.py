#  MORE ABOUT STRINGS :
# you cannot put double quote characters in double quote
# you can use escape sequence characters like \" 
# or enclose the string in single quote
# in python a string is like n array of characters

name = "Akanksha"

stat = '''hello my name is akanksha 
and i have an interest in "books"
i like to travel
and i love dogs'''
print(stat)

print(name[0]) 

print("let's use a for loop\n")
for character in stat:
    print(character)