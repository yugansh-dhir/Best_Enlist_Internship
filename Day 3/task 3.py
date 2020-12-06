# Exercise 1 - Write a Python script to merge two Python dictionaries
d1 = {'color': 'blue', 'fruit': 'apple'}
d2 = {'vegetable': 'cabbage', 'car': 'ford'}
d = d1.copy()
d.update(d2)
print(d)
print('\n')

# Exercise 2 - Write a Python program to remove a key from a dictionary
mydict = {'boy': 'girl', 'white': 'black', 'good': 'bad'}
print(mydict)
if 'good' in mydict:
    del mydict['good']
print(mydict)
print('\n')
# User Input
mydict={}
for i in range(5):
      Key=input("enter key")
      Value=input("enter value")
      mydict[Key]=Value
print(mydict)
if 'good' in mydict:
    del mydict['good']
print(mydict)
print('\n')

# Exercise 3 - Write a Python program to map two lists into a dictionary
keys = ['red', 'green', 'blue']
values = ['good','bad', 'ok']
color_dict = dict(zip(keys, values))
print(color_dict)
print('\n')

#Exercise 4 - Write a Python program to find the length of a set
#Create a set
myset = set([5, 10, 15, 20, 25, 30])
#Find the length use len()
print(len(myset))
print('\n')

#Exercise 5 - Write a Python program to remove the intersection of a 2nd set from the 1st set
myset1 = {5,10,15,20,25}
myset2 = {20,25,30,35,40}
print("Original sets:")
print(myset1)
print(myset2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
myset1.difference_update(myset2)
print(myset1)
myset1 = {5,10,15,20,25}
myset2 = {20,25,30,35,40}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(myset1-myset2)








