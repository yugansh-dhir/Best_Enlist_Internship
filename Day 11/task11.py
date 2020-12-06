#1 Write a program using zip() function and list() function
# create a merged list of tuples from the two lists given
nums1 = [1, 2, 3, 5, 25]
nums2 = [17, 8, 1, 20]
zipped_list = list(zip(nums1, nums2))
print(zipped_list, '\n')

#2 First create a range from 1 to 8. Then using zip
# merge the given list and the range together to create a new list of tuples
nums = [x for x in range(1, 9)]
nums1 = [80, 25, 38, 50, 5, 8, 89, 17, 22]
zipped_list = list(zip(nums, nums1))
print(zipped_list, '\n')

# 3 Using sorted() function, sort the list in ascending order
nums = [15, 9, 5, 4, 37]
print("Sorted list: ", sorted(nums))

# 4 Write a program using filter function
# filter the even numbers so that only odd numbers are passed to the new list
print("Enter the numbers: ")
temp = map(lambda x: int(x), input().split())
even_nums = list(filter(lambda x: x % 2 == 0, temp))
print('Even numbers are: ', even_nums)