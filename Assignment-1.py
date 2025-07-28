# 1. Display the current date and time
import datetime

now = datetime.datetime.now()
print("Current date & time :",now.strftime("%Y-%m-%d %H:%M:%S"))

'''output
Current date & time : 2025-07-27 16:27:06
'''


# 2. Area of a circle based on user input radius
from math import pi

r = float(input("Input the radius of the circle : "))
print(f"Area = {pi * r ** 2}")

'''output
Input the radius of the circle : 1.1
Area = 3.8013271108436504
'''


# 3. Number of days between two dates
from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
x = date2 - date1
print(f"{x.days} days")

'''output
9 days
'''


# 4. Volume of a sphere with radius six
from math import pi
radius = 6
volume = (4/3) * pi * (radius ** 3)
print("Volume of the sphere = ",volume)

'''output
Volume of the sphere = 904.7786842338603
'''


# 5. Difference between a given number and 17; if greater, return twice the absolute difference
n = int(input("Enter a number: "))
if n > 17:
    print(2 * abs(n - 17))
else:
    print(abs(n - 17))
    
'''output
Enter a number: 20
6
'''


# 6. Test if a number is within 100 of 1000 or 2000
n = int(input("Enter a number: "))
x = (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
print(x)

'''output
Enter a number: 998
True
'''


# 7. Sum of three given numbers; if values are equal, return three times their sum
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
if x == y == z:
    print(3 * (x + y + z))
else:
    print(x + y + z)

'''output
Input first number: 4
Input second number: 5
Input third number: 6
15
'''


# 8. Even/Odd tester for user-input number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

'''output
Enter a number: 4
Even
'''


# 9. Count the number 4 in a given list
x=[1, 4, 6, 7, 4, 4, 9]
print(x.count(4))

'''output
3
'''


# 10. Test if passed letter is a vowel
def is_vowel(char):
    return char.lower() in 'aeiouAEIOU'

letter = input("Enter a letter: ")
print(is_vowel(letter))

'''output
Enter a letter: A
True
'''

