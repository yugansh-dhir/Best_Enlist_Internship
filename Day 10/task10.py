# 1 Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
def characters(string):
    char = re.compile(r'[^a-zA-Z0-9.]')
    string = char.search(string)
    return not bool(string)
print(characters(input()))

#2 Write a Python program that matches a word containing 'ab'.
string = input()
patterns= '\w*ab\w*'
if re.search(patterns,string):
    print("Found A match")
else:
    print("Not Found")

#3 Write a Python program to check for a number at the end of a word/sentence.
def fun1(string):
    regex = re.compile(r".*[0-9]$")
    if regex.match(string):
        print("Found")
    else:
        print("Not Found")
a=input()
fun1(a)

#4 Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
a=input()
box=re.findall(r'[0-9]{1,3}',a)
print(box)

#5 Write a Python program to match a string that contains only uppercase letters
a =input()
pattern='^[A-Z_]*$'
if re.search(pattern,a):
    print("Found")
else:
    print("Not Found")



