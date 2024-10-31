#create a list
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print(fruits)

#create a list
list1 = ["apple", True, 23, "banana", "cherry", "mango", "orange"]
print(list1)

#legth of a list
print(len(fruits))

#access an item in a list
print(fruits[2])

#modify an element
new_item = fruits[2] = "grapes"
print(new_item)
print(fruits)

#remove an element
fruits.remove("grapes")
print(fruits)

#access element by using negative indexes
print(fruits[-2])

# # input the list as string
# string = input("Enter elements (Space-Separated): ")

# # split the strings and store it to a list
# lst = string.split()  
# print('The list is:', lst)   # printing the list


#list methods
#append method in list
fruits : list = ["apple", "cherry", "banana"] 
fruits.append("grapes") 
print(fruits)


#Extend method in the list.
cars : list  = ["Audi","BMW","Jaguar"]
other_cars = ["Maruti", "Tata"]
cars.extend(other_cars)
print(cars)

#insert method of list.
fruit : list = ["banana","cherry","grape"]
fruit.insert(1,"apple")
print(fruit)


# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split()  
print('The list is:', lst)   # printing the list





