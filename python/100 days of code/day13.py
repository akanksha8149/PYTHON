# String Methids in Python
# strings are immutable in python

# upper() and lower()
a = "!!!Akanksha!! !!Aditi!! !!Dikshita!!"
print(a.upper())
print(a.lower())

# rstrip()
print(a.rstrip("!"))

# replace()
print(a.replace("Akanksha","Aditi"))

# split()
print(a.split(" "))

# capitalize()
blog = "introduCtion to pythoN progrAmming"
print(blog.capitalize())

# center()
str1 = "Welcome to my python program !!!"
print(str1.center(50))
print(len(str1.center(50)))
print(len(str1))

# count()
print(a.count("!"))

# endswith()
str1 = "Welcome to my python program !!!"
print(str1.endswith("!!!"))

# find()
str2 = "Her name is Aditi. She is really good at heart"
print(str2.find("is"))

# isalnum() returns alphanumeric characters
str3 = "WelcomeToTheConsole00"
print(str3.isalnum())

# isalpha()
str4 = "Welcome00\n"
print(str4.isalpha())

# islower()
print(str4.islower())

# isprintable() returns True if all the values within the given string are printable, if not, then it returns false
print(str4.isprintable())

# isspace
str5 ="       "
print(str5.isspace())

# istitle() returns true onlu if the first letter of each word of the string is capitalized, else returns false
str6 = "World Health Organisation"
print(str6.istitle())

# startswith()
print(str2.startswith("Her"))

# swapcase()
b = "Python iS an Interpreted LanGuagE"
print(b.swapcase())

# title()
print(str2.title())




