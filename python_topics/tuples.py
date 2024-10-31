list1:list = ["apple", "banana", "mango", "orange"]
tuples_list = tuple(list1)
print(tuples_list)


fruits: tuple[int | str, ...] = (1, 2, 3, 4, "apple", "mango")
print(fruits)
print(type(fruits))


#convert tuple to list

fruits: tuple[int | str, ...] = (1, 2, 3, 4, "apple", "mango", "bananana")
print(fruits)
print(type(fruits))

list1 : list = list(fruits)
print(list1)
print(type(list1))
list1[0] = 23
print(list1)
fruits = tuple(list1)
print(fruits)


# #concatination of 2 tuples
tuple1 = (1,2,3,4,5)
tuple2 = ("hina", "komal")
tuple3 = (tuple1 + tuple2)
print(tuple3)

# #access an element to the concatinated tuple 
print(tuple3[3])


tuple1 = (1,2,3,4,5)
tuple2 = ("hina", "komal")
tuple3 = (tuple1 , tuple2)
print(tuple3)

# #access an element to the  nested tuple 
print(tuple3[1])
print(tuple3[0])


# #Repetation in tuple
tuple4 = ("apple",)*0
print(tuple4)

# #slicing
tuple5 = ("apple", "banana", "mango", "orange", 1,2,3,4,5)
print(tuple5)
print(tuple5[2:8])
print(tuple5[::-2])
print(tuple5[:])

tuple6 = ("hina", "kashaf")
print(tuple6)

#it generate error because tuple delete not allowed
# del tuple6
# print(tuple6)

var = ("uzair", "for", "uzair")
print(var)


var: tuple[int | str | float, ...] = (2, 3, "uzair", "for", "uzair")
print(type(var))
print(var)

# values: tuple[int | str, ...] = (1, 2, 4, "uzair", "rafay")
# print(values)

#convert tuple to list add an item in the list and then change it in tuple again and tuple is immutable so we ca covert first it in list and then chage it
tu: tuple[int | str, ...] = (1, 2, 3, 4, 6, "uzair")
print(tu)
list1 = list(tu)
print(list1)
list1.append("ali")
print(list1)
tu1: tuple[int | str, ...] = tuple(list1)
print(tu1)

# # Code for concatenating 2 tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'uzair')
 
# Concatenating the above two
result = (tuple1 + tuple2)
print(result)
print(result[5])


# # Code for creating nested tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'uzair')
 
tuple3 = (tuple1, tuple2)
print(tuple3)
print(tuple3[1])

#Repetation
# Code to create a tuple with repetition
tuple3 = ('ayesha', "komal") * 5
print(tuple3)

#Slicing
tuple1 = (1, 3, 2, 3, 5, 6, 7, 7, 8, 9, 10,66,77)
print(tuple1[::3])

#Deleting

# Code for deleting a tuple
# tuple3 = (0, 1)
# print(tuple3)
# del tuple3
# print(tuple3)
# print(tuple3)  # This will raise an error since tuple3 is deleted


#Finding the length
# Code for printing the length of a tuple
# tuple2 = ('python', 'uzair',"hina")
# print(len(tuple2))


# Tuple with different datatypes
tuple_obj = ("immutable", True, 23)
print(tuple_obj)