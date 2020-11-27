# Exercise 1 - Create a function getting two integer inputs from user. & print the following:
# Addition of two numbers is +value
# Subtraction of two numbers is +value
# Division of two numbers is +value
# Multiplication of two numbers is +value
# Here the value represents math function associated
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print('\n')
def my_arithmetic(m,n):
    print("Addition of two numbers is: ", m+n)
    print("Subtraction of two numbers is: ", m-n)
    print("Division of two numbers is: ", m/n)
    print("Multiplication of two numbers is: ", m*n)
my_arithmetic(a,b)
print('\n')

#Exercise 2 - Create a function covid( ) & it should accept patient name, and body temperature,
# by default the body temperature should be 98 degree
patient_name = ("Enter the name of patient: ")
def covid(patient_name,body_temp=98):
    print(patient_name,"'s body temperature is ",body_temp, "degrees")
covid("Yugansh")