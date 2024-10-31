#Print simple string in python.

string1 = 'hello world'
print(string1)

#find type by using type function.

print("hello")
print(type(string1))

#use single quote and double quote to write a sring

String1 = "GeeksForGeeks"
print("Initial String: ", String1)

# Printing First character.

print("First character of String is: ", String1[-5])

#Printing 3rd to 12th character

print("\nSlicing characters from 3-12: ")
print(String1[3:12:2])

#slicing string
# Printing characters between
# 3rd and 2nd last character

print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:8:2])


# #Program to reverse a string

gfg = "geeksforgeeks"
print(gfg[::-1])

#convert a string into a list and then change or update any value in a string and then convert it inti a string.

String1 = "GeeksForGeeks"
list1 = list(String1)
list1[2] = 'p'
String2 = (list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)

# Deleting a character
# Python Program to delete
# character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# print("Deleting character at 2nd Index: ")
# del String1[2]
# print(String1)
# if we try to delete  a character in a string then an error generated because string is immutable and they cannot allow to delete a string or its item.


# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

string2 = "hello world"
print(string2[0:16])


# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m \'a\' Geek'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the
# use of Tab
String1 = "Hi\tGeeks"
print("\nTab: ")
print(String1)

# Printing Paths with the
# use of New Line
String1 = "Python\nGeeks"
print("\nNew Line: ")
print(String1)

#case changing string methods in python
# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:")
print(text.title())

print("hello")
# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)

#using endswith
string = "geeksforgeeks"
print(string.endswith("geek"))


#string endswith in different cases
string1 = "hello world"
result = string1.endswith(' world', 5)
print(result)

#string endswith in different cases
string1 = "hello world"
result = string1.endswith('world', 6, 11)
print(result)




print("hy")
#python strings isalpha() method use.
# checking for alphabets
string = 'Ayush'
print(string.isalpha())

string = '0212'
print(string.isalpha())

# checking if space is an alphabet
string = 'Ayush Saxena'
print( string.isalpha())

#in python isalphanum
# here a,b and c are characters and 1,2 and 3
# are numbers
string = "abcdefghi237263271"
print(string.isalnum())


#python string is alphadecimal method

s = "12345"
print(s.isdecimal())

# contains alphabets
s = "12geeks34"
print(s.isdecimal())

# contains numbers and spaces
s = "12/34"
print(s.isdecimal())


# string which is to be stripped
string = "geeks for geeks"

# Removes given set of characters from
# right.
print(string.rstrip('ske'))