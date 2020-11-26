
# 1. Write a program to create a list of n integer values and do the following

A=[]
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    A.append(ele)  # adding the element

# Add an item to the list(using function)
A.insert(2,78)
# Delete(using function)
del A[4]
# Store the smallest number from the list to a variable
lo=min(A)
# Store the largest number from the list to a variable
hi=max(A)

print(A[0:7])
print(lo)
print(hi)


# 2. Create a tuple and print the reverse of created tuple
tup=('s', '6','1', 'u','o')
rtup=tup[::-1]
print(rtup)


# 3. Create a tuple and convert tuple into list
B=[]
tup=('s', '6','1', 'u','o')
for i in range(5):
    B.append(tup[i])

print(B[0:5])