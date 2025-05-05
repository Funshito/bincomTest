

mondayColors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

tuesdayColors = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']

wednesdayColors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']

thursdayColors = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

fridayColors = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']


#question 1
import statistics

monday = statistics.median(mondayColors)
tuesday = statistics.median(tuesdayColors)
wednesday = statistics.median(wednesdayColors)
thursday = statistics.median(thursdayColors)
friday = statistics.median(fridayColors)

print("mean color for monday is: ", monday)
print(f"mean color for tueday is: {tuesday}")
print(f"mean color for wednesday is: {wednesday}")
print(f"mean color for thursday is: {thursday}")
print(f"mean color for friday is: {friday}")





#question 2
from collections import Counter
weekColor = []


weekColor.extend(mondayColors)
weekColor.extend(tuesdayColors)
weekColor.extend(wednesdayColors)
weekColor.extend(thursdayColors)
weekColor.extend(fridayColors)

counts = {}
for color in weekColor:
    counts[color] = counts.get(color, 0) + 1
most_common = max(counts, key=counts.get)
print("Most frequent color of the week:", most_common)
   
   
   
   
   
   
   
# question 8


import random

binary_number = ''.join(random.choice('01') for _ in range(4))

decimal_number = int(binary_number, 2)

print("Random Binary Number:", binary_number)
print("Decimal Equivalent:", decimal_number)



 # question 9

def fibonacci_sum(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return sum(fib)

result = fibonacci_sum(50)
print("Sum of first 50 Fibonacci numbers:", result)


# question 7


def search(arr, target, index=0):
    # Base case: If index reaches the end of the list, return -1 (not found)
    if index >= len(arr):
        return -1
    
    # If the current element matches the target, return the index
    if arr[index] == target:
        return index
    
    # Recursively search in the rest of the list
    return search(arr, target, index + 1)

# Get user input
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

# Perform recursive search
result = search(numbers, target)

# Print the result
if result != -1:
    print(f"Number {target} found at index {result}")
else:
    print(f"Number {target} not found in the list")