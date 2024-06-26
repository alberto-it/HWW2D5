print()
"""
Lesson 5: Assignments | Python Functions
1. The Calculator App
Task 1: Create functions for each arithmetic operation.
"""
def add(x, y):
    return x + y
def diff(x, y):
    return x - y
def times(x, y):
    return x * y
def div(x, y):
    return x / y
"""
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.
"""
while True:
    try:
        num1 = float(input(" First  Number: "))
        num2 = float(input(" Second Number: "))
        break
    except ValueError:
        print("Numbers Only... Please Start Over")
        
operators = ['add', 'subtract', 'multiply', 'divide']
operation = input(f"Enter Operation Choice ({", ".join(operators)}): ").lower()
    
if operation == operators[0]:
    result = add(num1, num2)
elif operation == operators[1]:
    result = diff(num1, num2)
elif operation == operators[2]:
    result = times(num1, num2)
elif operation == operators[3]:
    if num2 != 0:
        result = div(num1, num2)
    else:
        result = "Error | Cannot divide by zero!"
else:
    result = "Error | Invalid Operation Choice!"

print(f"Result: {result}\n")
"""
2. The Shopping List Maker
Task 1: Write a function that lets the user add items to a list.
"""
def add_item(list):
    while True:
        item = input("Enter item to add to list (or enter nothing to quit): ")
        if item:
            list.append(item)
        else:
            break
test = []
add_item(test)
print()
"""
Task 2: Include a feature to remove items from the list.
"""
def remove_item(list):
    while True:
        if not list:
            print("List is Empty\n")
            break
        i = int(input("Enter Item Number to be remove or 0 to Exit: ")) - 1
        if i < 0:
            break
        if i >= len(list):
            print("Item # is too high. Only", len(list), "items are currently on the list.")
        else:
            item = list.pop(i)
            print(item, "removed from the list.", "Remove another?" if list else "")

remove_item(test)
print()
"""
Task 3: Add a function that prints out the entire list in a formatted way.
"""
def print_list(list):
    if list:
        print("\nList:")
        for i, item in enumerate(list):
            print(i+1, "-", item)
    else:
        print("List is empty!")
        
print_list(test)
print()
"""
3. The Grade Analyzer
Task 1: Code a function to calculate the average grade.
"""
def avg_grade(*grades):
    return sum([grade for grade in grades])/len(grades) if grades else None

print(avg_grade(95, 55, 75, 81), "\n", avg_grade(), "\n")
"""
Task 2: Implement a function to find the highest and lowest grade.
"""
def high_low(*grades):
    if not grades:
        return None, None 
    return max(grades), min(grades)  

high, low = high_low(95, 55, 75, 81)
print("Highest:", high, "\nLowest:", low, "\n")
"""
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
"""
def letter_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'
    return 'F'

print(high, "is a letter grade of", letter_grade(high))
print(low,  "is a letter grade of", letter_grade(low) )
print()
