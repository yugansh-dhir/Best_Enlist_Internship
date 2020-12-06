# 1 List down all the error types and check all the errors using a py-thon program for all errors

# Zero Division Error
try:
    print(50 / 0)
except ZeroDivisionError:
    print("Unable to Divide By Zero")

# Index Error
arr = [15, 20, 25]
try:
    print(arr[3])
except IndexError:
    print('Index not found in array')

# Key Error
dicti = {"1" : 'a', "2" : 'b', "3" : 'c'}
try:
    print(dicti["4"])
except KeyError:
    print('Key not found in dictionary')

# Module Not Found Error
try:
    import flask
except ModuleNotFoundError:
    print("Module not found")

#2  Design a simple calculator app with try and except for all use cases
symbols = '+ - x / % \n'
try:
    input_one = int(input('Enter your 1st input :'))
    print(symbols)
    chosen_symbol = input('Choose your symbol from above :')
    input_two = int(input('Enter your 2nd input :'))
    if chosen_symbol in symbols:
        if chosen_symbol == '+':
            print(input_one, '+', input_two, '=',input_one + input_two)
        elif chosen_symbol == '-':
            print(input_one, '-', input_two, '=',input_one - input_two)
        elif chosen_symbol == 'x':
            print(input_one, 'x', input_two, '=',input_one * input_two)
        elif chosen_symbol == '/':
            print(input_one, '/', input_two, '=',input_one / input_two)
        elif chosen_symbol == '%':
            print(input_one, '%', input_two, '=',input_one % input_two)
except ValueError:
    print("Enter Proper Numbers For Input!")
except ZeroDivisionError:
    print("Unable to Divide by Zero (0) !")

# 3 - Print one message if the try block raises a NameError and another for other errors
try:
    print(newArr)
except NameError:
      print("newArr is not defined")
except:
      print("Unknown Error")

#4 When try-except scenario is not required?
print('try-except scenario is not required if you are not going to have any runtime error in your python program or when exception handling is not required. If there is any possibility that there might exist a runtime error, you must use a try - except scenario in order to avoid a crash, and guide the user with proper message.')

#5 Try getting an input inside the try catch block
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")