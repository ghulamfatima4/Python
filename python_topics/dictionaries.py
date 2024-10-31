dict = {'1' : 'apple', '2' : 'mango', 'fruit' : 'banana'}
print(dict)
print(type(dict))

#demonstrates creating dictionaries with different types of keys.
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {"Name": 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
print(Dict[1])
print(Dict["Name"])

#Nested dictionaries
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)

#accessing elements in nested dictonaries
print(Dict[1])
print(Dict[2])
print(Dict[3]['A'])

#access a value in a dictionary.
print(Dict[1])
print(Dict[2])
print(Dict[3]['A'])
print(Dict[3]['B'])

#deleting element in dictionaries by del keyword in python
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Dictionary =")
print(Dict)
del(Dict[1])
del(Dict[3])
# del(Dict[4])
#if we want to delete a value that cannot exist in the dictioarie.
#then it shows an error
print("Data after deletion Dictionary=")
print(Dict)

fruits : dict = {'A' : 'Apple', 'B' : 'banana', 'C' : 'mango'}
print(fruits)


#Dictioanrie methods
# Python program to demonstrate working of
# dictionary clear()
text = {1: "geeks", 2: "for"}
print(text)
text.clear()
print('text =', text)

#python dictionarie copy
original = {1: 'geeks', 2: 'for'}

# copying using copy() function
new = original.copy()

# removing all elements from the list
# Only new list becomes empty as copy()
# does shallow copy.
# new.clear()

print('new: ', new)
print('original: ', original)

dictionary = {'a' : 'hina', 'b' : 'faiza'}
new = dictionary.copy()
print(dictionary)
print(new)
new.clear()
print(new)
print(dictionary)

#fromkeys method in dictionaries
new = ('1', '2','3','4','5')
new_dict = dict.fromkeys(new, 'hello')
print(new_dict)


#get method in python dictionaries
d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))


d = {1: '001', 2: '010', 3: '011'}

print(d.get(4, "Not found"))
print(d.get(3, "Not found"))


test_dict = {'Gfg' : {'is' : 'best'}}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# using nested get()
# Safe access nested dictionary key
res = test_dict.get('Gfg', {}).get('is')
  
# printing result
print("The nested safely accessed value is :  " + str(res))



#in dictionaries to remove items through pop method
# inializing dictionary student 
student = {"rahul":7, "Aditya":1, "Shubham":4} 

# priting original dictionary 
print(student) 

# using dictionary pop 
suspended = student.pop("rahul")
suspended2 = student.pop("Shubham")

# checking key of the element 
print("suspended student roll no. = "+ str(suspended)) 
print("suspended student roll no. = "+ str(suspended2)) 

# printing list after performing pop() 
print("remaining student" + str(student))