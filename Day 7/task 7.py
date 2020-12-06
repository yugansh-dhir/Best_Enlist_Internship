import module1
module1.fun1("yugansh")

#============
import random
import sys
#=============

import module1 as md
md.fun1("Yugansh Dhir")


from module1 import fun1
fun1("Best Enlist")
#------------------------

#PIP : PIP is a package manager for Python packages, or modules
#We can download a package by using pip install <module name>
#Example: pip install pandas
#Pip list command is used to list the packages present in the system


#Create a python module with list and import the module in another .py file and change the value in list
from module1 import list
for i in range(len(list)):
    list[i]=list[i]+2
print(list)

#Remember Backend Module Things doesnot changes

#---------------
#Install pandas package (try to import the package in a python file

#pip install pandas

#----------------
#Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
'''
Python defines a set of functions that are used to generate or manipulate random numbers. This particular type of functions are used in a lot of games, lotteries or any application requiring random number generation.
Randon Number Operations :
1. choice() :- This function is used to generate 1 random number from a container.
2. randrange(beg, end, step) :- This function is also used to generate random number but within a range specified in its arguments. This function takes 3 arguments, beginning number (included in generation), last number (excluded in generation) and step ( to skip numbers in range while selecting).
'''
import random
n=10
while(n):
    print(random.randrange(1,100, 3))
    n=n-1
#OR

print(random.randint(1,100))

#----------------

#Import sys package and find the python path
import sys
print(sys.path)

#--------------
#Try to install a package and uninstall a package using pip
# pip uninstall pandas
