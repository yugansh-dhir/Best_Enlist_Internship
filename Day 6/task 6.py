import math
# Write a program to loop through a list of numbers and add +2 to every value to elements in list
original_list = [15, 20, 85, 152, 305, 500]
print("The original list is : " + str(original_list))
# using list comprehension
# adding K to each element
res = [x + 2 for x in original_list]
# printing result
print("The list after adding 2 to each element : " + str(res))

# Write a program to get the below pattern
for i in range(5, 0,-1):
    for j in range(i, 0,-1):
        print(j, end = '')
print()


# 6a
#Program to Print the Fibonacci sequence
terms = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# Explain Armstrong number and write a code with a function
# Armstrong Number - an armstrong number in a given number base b is a number
# that is the sum of its own digits each raised to the power of the number of digits.
num = int(input("Enter a number: "))
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# Write a program to print the multiplication table of 9
num = 9
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# Check if a program is negative or positive
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# 6b
# Write a program to convert the number of days to ages
days_in_a_week = 7
# Function to find
# year, week, days
def find(number_of_days):
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
               days_in_a_week)
    days = (number_of_days % 365) % days_in_a_week
    print("years = ", year,
          "\nweeks = ", week,
          "\ndays = ", days)
number_of_days = 500
find(number_of_days)

# Solve Trigonometry problem using math function write a program to solve us-ing math function
# sin() and cos()

a = math.pi/10
print ("The value of sine of pi/10 is : ", end="")
print (math.sin(a))
print ("The value of cosine of pi/10 is : ", end="")
print (math.cos(a))


# 6c
# Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ") # User input
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")