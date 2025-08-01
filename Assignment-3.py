# Q1. Demonstrate following list methods in Python
lst = [5, 2, 9, 1, 5, 6]

print("Original list:", lst)

# append(): Adds an item to the end of the list
lst.append(10)
print("After append(10):", lst)

# extend(): Adds items of a list to the end
lst.extend([7, 8])
print("After extend([7, 8]):", lst)

# insert(): Inserts an item at a specified index
lst.insert(2, 15)
print("After insert(2, 15):", lst)

# remove(): Removes the first occurrence of the specified value
lst.remove(5)
print("After remove(5):", lst)

# pop(): Removes and returns item at given index (default last)
popped_item = lst.pop(3)
print("After pop(3):", lst)
print("Popped item:", popped_item)

# index(): Returns index of the first occurrence of value
y = lst.index(6)
print("Index of 6:", y)

# count(): Returns the number of occurrences of the specified item
x = lst.count(5)
print("Count of 5:", x)

# sort(): Sorts the list in ascending order
z = lst.copy()
z.sort()
print("Sorted list (ascending):", z)

'''
# sort in descending order
l = lst.copy()
l.sort(reverse=True)
print("Sorted list (descending):", l)
'''

# reverse(): Reverses the list in place
li = lst.copy()
li.reverse()
print("Reversed list:", li)

# copy(): Returns a shallow copy of the list
print("Copied list:", lst.copy())

# clear(): Removes all items from the list
lst.clear()
print("After clear():", lst)

'''OUTPUT
Original list: [5, 2, 9, 1, 5, 6]
After append(10): [5, 2, 9, 1, 5, 6, 10]
After extend([7, 8]): [5, 2, 9, 1, 5, 6, 10, 7, 8]
After insert(2, 15): [5, 2, 15, 9, 1, 5, 6, 10, 7, 8]
After remove(5): [2, 15, 9, 1, 5, 6, 10, 7, 8]
After pop(3): [2, 15, 9, 5, 6, 10, 7, 8]
Popped item: 1
Index of 6: 4
Count of 5: 1
Sorted list (ascending): [2, 5, 6, 7, 8, 9, 10, 15]
Reversed list: [8, 7, 10, 6, 5, 9, 15, 2]
Copied list: [2, 15, 9, 5, 6, 10, 7, 8]
After clear(): []
'''


# Q2. Remove 0th, 4th and 5th elements
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del colors[5]
del colors[4]
del colors[0]
print(colors)

'''OUTPUT
['Green', 'White', 'Black']
'''

# Q3. Remove even numbers from list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = [x for x in nums if x % 2 != 0]  #List comprehension: for each x, keep if x mod 2 is not 0 (odd)
print(odd_nums)

'''OUTPUT
[1, 3, 5, 7, 9]
'''

# Q4. Shuffle a list
import random
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

'''OUTPUT
[3, 2, 1, 5, 4]
'''

# Q5. Check if all numbers in a list are prime
def is_prime(n):
    # Returns True if n is a prime number; False otherwise.
    # Step 1: n must be greater than 1 (since 0/1 are not prime)
    # Step 2: For all i from 2 to sqrt(n), n should not be divisible by i.
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

def all_primes(lst):
    # Returns True if every element in lst is prime. False if any element is non-prime.
    return all(is_prime(x) for x in lst)     # Step 1: Checks every value x in the list with 'is_prime'

# Step 2: Test cases for different lists.
print("Output 1:", all_primes([0, 3, 4, 7, 9]))   # Output False. 0, 4, 9 are not prime.
print("Output 2:", all_primes([3, 5, 7, 13]))     # Output True. All numbers are prime.
print("Output 3:", all_primes([1, 5, 3]))         # Output False. 1 is not prime.

'''OUTPUT
Output 1: False
Output 2: True
Output 3: False
'''

# Q6. Difference between two lists
a = [1, 2, 3, 4]
b = [2, 4, 6]
diff = list(set(a) - set(b))
print(diff)

'''OUTPUT
[1, 3]
'''

# Q7. Flatten a shallow (single-level nested) list
lst = [[1, 2], [3, 4], [5, 6]]                # Step 1: List of lists (each sublist contains two elements)
flat = [item for sublist in lst for item in sublist] # Step 2: Nested list comprehension: for every sublist, extract each item
print(flat)                                   # Step 3: Output: single list including all elements, in order

'''OUTPUT
[1, 2, 3, 4, 5, 6]
'''

# Q8. Find second smallest element in the list
nums = [4, 1, 7, 3, 2]                        # Step 1: Input list with unsorted numbers
print(sorted(nums)[1])                        # Step 2: Sort ascending, then access index 1 for second smallest

'''OUTPUT
2
'''

# Q9. Check if a sublist exists within main list
def has_sublist(lst, sub):
    # Returns True if sublist 'sub' appears in list 'lst' in consecutive positions
    # The range sets up windows of len(sub) and checks each one
    return any(lst[i:i+len(sub)] == sub for i in range(len(lst)-len(sub)+1))

# Step 2: Output True if [2, 3] is a sublist of [1, 2, 3, 4], otherwise False.
print("Output 1:", has_sublist([1, 2, 3, 4], [2, 3]))  # True because [2, 3] is found
print("Output 2:", has_sublist([1, 2, 3], [4]))        # False, [4] not in [1, 2, 3]

'''OUTPUT
Output 1: True
Output 2: False
'''

# Q10. Concatenate each string in list with numbers from 1 to n
lst = ['p', 'q']                               # Step 1: List with two string values
n = 5                                          # Step 2: Specify number range (1-5)
# Step 3: List comprehension iterates for j from 1 to 5, and for each j, for every i in lst, makes i+str(j)
res = [i + str(j) for j in range(1, n+1) for i in lst]
print(res)                                     # Step 4: Output is concatenation in the order 'p1', 'q1', 'p2', 'q2', ...

'''OUTPUT
['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''

# Q11. Find items present in only one of the two lists
a = ['a', 'b', 'c', 'd', 'e']                  # First input list (reference/set A)
b = ['d', 'e', 'f', 'g', 'h']                  # Second input list (reference/set B)
# Step 1: Missing are values in a but not in b. Calculated as set(a) - set(b)
print("Missing:", list(set(a) - set(b)))
# Step 2: Additional are values in b but not in a. Calculated as set(b) - set(a)
print("Additional:", list(set(b) - set(a)))

'''OUTPUT
Missing: ['b', 'a', 'c']
Additional: ['f', 'g', 'h']
'''

# Q12. Split list so each sublist contains every Nth element from the original, starting from index i (where i = 0 to n-1)
lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']  # Step 1: List of single-character strings
n = 3                                                            # Step 2: Number of groups to create
# Step 3: For each i in 0 to n-1, slice the list taking every nth element, beginning at i
res = [lst[i::n] for i in range(n)]
print(res)                                                       # Step 4: Output is a list of groups, each containing every Nth item

'''OUTPUT
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
'''
