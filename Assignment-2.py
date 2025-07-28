# 1. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list of those numbers.
n = input("Enter comma-separated numbers: ") 
print("List of numbers:", n.split(','))

'''output
Enter comma-separated numbers: 4,5,6,7,8
List of numbers: ['4', '5', '6', '7', '8']
'''


# 2. Write a Python program to sum all the items in a list.
l = [1, 2, 3, 4, 5]
print("Sum of the list:", sum(l))

'''output
Sum of the list: 15
'''


# 3. Write a Python program to multiply all the items in a list.
import math

x = [1, 2, 3, 4, 5]
print("Product of the list:", math.prod(x))

'''output
Product of the list: 120
'''


# 4. Write a Python program to get the largest number from a list.
num = [1, 2, 3, 4, 5]
print("Largest number in the list:", max(num))

'''output
Largest number in the list: 5
'''


# 5. Write a Python program to get the smallest number from a list.
li = [1, 2, 3, 4, 5]
print("Smallest number in the list:", min(li))

'''output
Smallest number in the list: 1
'''


# 6. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
count = 0
s = ['abc', 'xyz', 'aba', '1221']
for i in s:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print("Count of strings with same first and last characters:", count)

'''output
Count of strings with same first and last characters: 2
'''


# 7. Write a Python program to remove duplicates from a list.
lst = [1, 2, 2, 3, 4, 4, 5] 
print("List after removing duplicates:", list(set(lst)))

'''output
List after removing duplicates: [1, 2, 3, 4, 5]
'''


# 8. Write a Python program to check if a list is empty or not.
t = []
if not t:
    print("The list is empty.")
else:
    print("The list is not empty.")

'''output
The list is empty.
'''


# 9. Write a Python program to clone or copy a list.
original_list = [1, 2, 3, 4, 5]
print("Cloned list:", original_list.copy())

'''output
Cloned list: [1, 2, 3, 4, 5]
'''


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
words_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
n = 5
for word in words_list:
    if len(word) > n:
        print(word)

'''output
banana
cherry
'''


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8]
if (set(l1) & set(l2)):
    print("True")
else:
    print("False")

'''
#Same program , different technique
l1 = [1, 2, 3, 4, 5]
l2 = [7, 6, 7, 8, 4]
for x in l1:
    for y in l2:
        if x==y:
            print("True")
'''
'''output
True
'''
