

mondayColors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

tuesdayColors = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']

wednesdayColors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']

thursdayColors = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

fridayColors = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']


#question 1

import math
monedayLen = len(mondayColors)
mondayNum = monedayLen/2
MonNum = math.ceil(mondayNum)
MondayMean = mondayColors[MonNum]
print(f"Mean for Monday: {MondayMean}")

tuesdayLen = len(tuesdayColors)
tuesdayNum = tuesdayLen/2
tuesNum = math.ceil(tuesdayNum)
tuesdayMean = tuesdayColors[tuesNum]
print(f"Mean for Tuesday: {tuesdayMean}")

wednesdayLen = len(wednesdayColors)
wednesdayNum = wednesdayLen/2
wedNum = math.ceil(wednesdayNum)
wednesdayMean = wednesdayColors[wedNum]
print(f"Mean for Wednesday: {wednesdayMean}")

thursdayLen = len(thursdayColors)
thursdayNum = thursdayLen/2
thurNum = math.ceil(thursdayNum)
thursdayMean = thursdayColors[thurNum]
print(f"Mean for Thursday: {thursdayMean}")

fridayLen = len(fridayColors)
fridayNum = fridayLen/2
friNum = math.ceil(fridayNum)
fridayMean = fridayColors[friNum]
print(f"Mean for Friday: {fridayMean}")


import statistics

# monday = statistics.median(mondayColors)
# tuesday = statistics.median(tuesdayColors)
# wednesday = statistics.median(wednesdayColors)
# thursday = statistics.median(thursdayColors)
# friday = statistics.median(fridayColors)

# print("mean color for monday is: ", monday)
# print(f"mean color for tueday is: {tuesday}")
# print(f"mean color for wednesday is: {wednesday}")
# print(f"mean color for thursday is: {thursday}")
# print(f"mean color for friday is: {friday}")





#question 2

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
   
   
   
   
   
#question 3
weekColor.sort()
weekLen = len(weekColor)
medianNumber = weekLen/2
medianNum = math.ceil(medianNumber)
medianColor = weekColor[medianNum] 
print(f"Median color is: {medianColor}")





#question 4
# VarianceColor = statistics.variance(weekColor)
# print(f"Variance is : {VarianceColor}")





#question 5
probability = weekColor.count('RED') / len(weekColor)
print(f"Probability of random red is: {probability}")







#question 6
from collections import Counter






#question 7

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def search(arr, target, index=0):
    
    if index >= len(arr):
        return -1
    
    if arr[index] == target:
        return index
    
    return search(arr, target, index + 1)
    
try:
    user_input = int(input("Enter a number to search for: "))
    result = search(numbers, user_input)
    
    if result != -1:
        print(f"Number {user_input} found at index {result}")
    else:
        print(f"Number {user_input} was not found in the list.")
except:
    print("Please enter a valid number")



# question 8


import random

binary_number = ''.join(random.choice('01') for _ in range(4))

decimal_number = int(binary_number, 2)

print("Random Binary Number:", binary_number)
print("Base Conversion:", decimal_number)



 # question 9

def fibonacci_sum(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return sum(fib)

result = fibonacci_sum(50)
print("Sum of first 50 Fibonacci numbers:", result)


