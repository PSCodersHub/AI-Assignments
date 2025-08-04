# Q1. Write a program to implement bubble sort using Python.

L=eval(input("Enter the elements: "))
n = len(L)
for i in range(0, n-1):
    # Last i elements are already sorted
    for j in range(0, n-1):
        # Swap if the element found is greater than the next
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print("The Sorted list is:", L)

'''OUTPUT
Enter the elements: [45, 84, 25, 4, 8]
The Sorted list is: [4, 8, 25, 45, 84]
'''


# Q2. Write a program to implement insertion sort using Python.

L=eval(input("Enter the elements: ")) 
n=len(L) 
for j in range(1,n):
    temp=L[j]
    prev=j-1
    while prev>=0 and L[prev]>temp:
        L[prev+1]=L[prev]
        prev=prev-1
        L[prev+1]=temp
print("The sorted list is :",L)

'''OUTPUT
Enter the elements: [25, 2, 7, 84, 55]
The sorted list is : [2, 7, 25, 55, 84]
'''


# Q3. Write a program to implement linear search using Python.

L = eval(input("Enter the elements: "))
item = eval(input("Enter the item to search for: "))
n = len(L)
found = False

for i in range(n):
    if L[i] == item:
        print(f"Item {item} found at index {i}")
        found = True
        break

if not found:
    print(f"Item {item} not found in the list")

'''OUTPUT
Enter the elements: [2, 3, 4, 10, 40]
Enter the item to search for: 4
Item 4 found at index 2
'''


# Q4. Write a program to implement binary search using Python.

L = eval(input("Enter the sorted elements: "))
item = eval(input("Enter the item to search for: "))
start = 0
end = len(L) - 1
found = False

while start <= end:
    mid = (start + end) // 2
    if L[mid] == item:
        print(f"Item {item} found at index {mid}")
        found = True
        break
    elif L[mid] < item:
        start = mid + 1
    else:
        end = mid - 1

if not found:
    print(f"Item {item} not found in the list")

'''OUTPUT
Enter the sorted elements: [10, 20, 30, 40]
Enter the item to search for: 40
Item 40 found at index 3
'''

#===========================================================================================================
#=======================================LINE-BY-LINE EXPLANATION PART=======================================
#===========================================================================================================

# Q1. Write a program to implement bubble sort using Python.

L=eval(input("Enter the elements: "))  # Take input list from user and convert string to list using eval()
n = len(L)  # Store the length of the list in variable n
for i in range(0, n-1):  # Outer loop runs n-1 times (for n-1 passes)
    # Last i elements are already sorted
    for j in range(0, n-1):  # Inner loop to compare adjacent elements
        # Swap if the element found is greater than the next
        if L[j] > L[j+1]:  # Compare current element with next element
            L[j], L[j+1] = L[j+1], L[j]  # Swap elements if they are in wrong order
print("The Sorted list is:", L)  # Print the final sorted list

'''OUTPUT
Enter the elements: [45, 84, 25, 4, 8]
The Sorted list is: [4, 8, 25, 45, 84]
'''


# Q2. Write a program to implement insertion sort using Python.

L=eval(input("Enter the elements: "))  # Take input list from user and convert to list using eval()
n=len(L)  # Store the length of the list in variable n
for j in range(1,n):  # Start from second element (index 1) and go till end
    temp=L[j]  # Store current element in temporary variable
    prev=j-1  # Set prev to the index just before current element
    while prev>=0 and L[prev]>temp:  # While previous element exists and is greater than temp
        L[prev+1]=L[prev]  # Shift the larger element one position to the right
        prev=prev-1  # Move to the previous element
        L[prev+1]=temp  # Insert temp at the correct position
print("The sorted list is :",L)  # Print the final sorted list

'''OUTPUT
Enter the elements: [25, 2, 7, 84, 55]
The sorted list is : [2, 7, 25, 55, 84]
'''


# Q3. Write a program to implement linear search using Python.

L = eval(input("Enter the elements: "))  # Take input list from user and convert to list using eval()
item = eval(input("Enter the item to search for: "))  # Take the search item from user
n = len(L)  # Store the length of the list in variable n
found = False  # Initialize a flag variable to track if item is found

for i in range(n):  # Loop through each element in the list from index 0 to n-1
    if L[i] == item:  # Check if current element matches the search item
        print(f"Item {item} found at index {i}")  # Print the index where item is found
        found = True  # Set found flag to True
        break  # Exit the loop as item is found

if not found:  # If item was not found (found is still False)
    print(f"Item {item} not found in the list")  # Print message that item is not in list

'''OUTPUT
Enter the elements: [2, 3, 4, 10, 40]
Enter the item to search for: 4
Item 4 found at index 2
'''


# Q4. Write a program to implement binary search using Python.

L = eval(input("Enter the sorted elements: "))  # Take sorted input list from user using eval()
item = eval(input("Enter the item to search for: "))  # Take the search item from user
start = 0  # Initialize start pointer to first index of the list
end = len(L) - 1  # Initialize end pointer to last index of the list
found = False  # Initialize a flag variable to track if item is found

while start <= end:  # Continue searching while start pointer doesn't cross end pointer
    mid = (start + end) // 2  # Calculate middle index using integer division
    if L[mid] == item:  # Check if middle element is the search item
        print(f"Item {item} found at index {mid}")  # Print the index where item is found
        found = True  # Set found flag to True
        break  # Exit the loop as item is found
    elif L[mid] < item:  # If middle element is smaller than search item
        start = mid + 1  # Move start pointer to right half (mid + 1)
    else:  # If middle element is greater than search item
        end = mid - 1  # Move end pointer to left half (mid - 1)

if not found:  # If item was not found (found is still False)
    print(f"Item {item} not found in the list")  # Print message that item is not in list

'''OUTPUT
Enter the sorted elements: [10, 20, 30, 40]
Enter the item to search for: 40
Item 40 found at index 3
'''
