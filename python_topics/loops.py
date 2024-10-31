#loops in python
#for loop
#for loop for strings.

print("string iteration")
s = "Geeks"
for i in s:
    print(i)

#python for loop for range
for i in range(0,20,2):
    print(i)

#in python enumerate function is used to find index and value.
li = ["apple", "banana", "mango", "orange", "grapes"]
for i , a in enumerate(li):
    print(i, a)

#nested for loop
print("next line")
for i in range(1, 4):
    for j in range(5, 9):
        for k in range(5, 9):
            print(i, j, k)


#continue in python

for var in "Geeksforgeeks":
    if var == "e":
        continue
    print(var)


#break in python
for i in range(11):
    print(i)
    if i == 5:
        break


# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 'f':
        break

print("Out of for loop"    )
print()

i = 0


#while loops
# Python program to illustrate
# while loop
count = 0
while (count < 3):
    print("Hello Geek")
    count = count + 1

#infinite while loop
# age = 28

# # the test condition is always True
# while age > 19:
#     print('Infinite Loop')

#control statements in python
# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
        
    print('Current Letter :', a[i])
    i += 1
count = 0
list = ["apple", "mango", "ornge", "banana", "grapes"]
while count < len(list):
    if list[count] == "apple":
        continue
    print(list[count])
    count = count + 1
# List of fruits
fruits = ["banana", "apple", "mango", "orange"]

# Initialize index
index = 0

# List of fruits
fruits = ["banana", "apple", "mango", "orange"]

# Initialize index
index = 0

# While loop to access each item
while index < len(fruits):
    if fruits[index] == "orange":
        index += 1
        continue
    print(fruits[index])
    index += 1

condition = True

while condition:
    user_input = input("write your name: ")
    if user_input == "exit":
        condition = False
    print(input("write exit to close it"))