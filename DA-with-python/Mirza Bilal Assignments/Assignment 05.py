# ------------  Assignment 05 -------------

# QUESTION 1: Working with Lists

#     1.Create a list called numbers containing at least 8 integers.
#     2.Using a for loop, do the following:
#         o Print all numbers in the list.
#         o Print the sum of all numbers.
#         o Print only the even numbers.
#     Requirements:
#          Use at least one loop.
#          Use conditional statements.
#          Display clear output


numbers = [3, 6, 2, 55, 23, 11, 9, 22]  # list containing 8 integers
sum = 0

print("ALL NUMBERS IN THE LIST: ")

# for loop
for num in numbers:
    print(num)
    sum += num     # sum = sum + num   calculation

print("\nSUM OF ALL NUMBERS: ", sum)

print("\nEVEN NUMBERS: ")

# for loop and conditonal satatement
for num in numbers:
    if num % 2 == 0:
        print(num)
        
        



# QUESTION 2: Dictionary Basics
#     1.Create a dictionary called student with the following keys:
#         o name
#         o age
#         o course
#         o marks (must store a list of 3 marks)
#     2.Using loops:
#         o Print all keys and their values.
#         o Calculate the average of the marks.
#         o Display whether the student Passed (average ≥ 50) or Failed.
# Requirements:
#      Dictionary must contain a list.
#      Use loops to calculate the average.


# creating a distionary 
Student = { 
    "Name" : "Mirza Bilal Hussain",
    "Age" : 19,
    "Course" : "Python Programming",   
    "Marks" : [87, 67, 94]
}

# print all keys and values
print("STUDENT INFORMATION: ")

for key,value in Student.items():
    print(key, ":", value)

# Calculate the average of the marks.
total_marks = 0
# total marks
for mark in Student["Marks"]:
    total_marks += mark
# Average
average = total_marks / len(Student["Marks"])
print("\nAverage Marks: ", average)

# condition check pass or fail
if average >= 50:
    print("STATUS: PASSED")
else:
    print("STATUS: FAILED")    





# QUESTION 3: List of Dictionaries
#     1.Create a list called employees.
#     2.Each employee must be stored as a dictionary containing:
#         o name
#         o department
#         o salary
#     3.Using loops:
#         o Print details of all employees.
#         o Find the employee with the highest salary.
#         o Calculate the total salary expense.
# Requirements:
#      Minimum 3 employees.
#      Use comparison logic.
#      Use loops to process data.


# creating a list 
Employees = [
    {
        "Name" : "Mirza Bilal",         # distionary 01
        "Department" : "AI",
        "Salary" : 55000
    },
    {
        "Name" : "Sara",                # distionary 02
        "Department" : "IT",
        "Salary" : 35000
    }, 
    {
        "Name" : "Basit",               # distionary 03
        "Department" : "HR",
        "Salary" : 45000
    }
]


# details of all employees
print("EMPLOYEES DETAIL: \n")

for employee in Employees:
    print("Name: " , employee["Name"])
    print("Department: " , employee["Department"])
    print("Salary: " , employee["Salary"])
    print()
    
# employee with highest salary
highest_salary = 0
highest_employee = ""

for employee in Employees:                              # foor loop
    if employee["Salary"] > highest_salary:             # conditional statement
        highest_salary = employee["Salary"]      
        highest_employee = employee["Name"]

print("HIGHEST SALARY EMPLOYEE: " , highest_employee)
print("HIGHEST SALARY: " , highest_salary)





# QUESTION 4: While Loop with User Input
#     1.Ask the user to enter numbers.
#     2.Store the numbers in a list.
#     3.Stop when the user enters -1.
#     4.After the loop ends:
#         o Print the complete list.
#         o Print the largest number.
#         o Print the smallest number.
# Requirements:
#      Must use a while loop.
#      Must store input in a list.
#      Handle user input correctly. 


numbers = []

# while loop
while True:
    number = int(input("Enter a number (-1 to stop): "))
    
    if number == -1:    # stop when user enter -1
        break
    
    numbers.append(number)      # store number in the list
    
    print("\nNumbers: ", numbers)
    
    
# largest number and smallest numbers
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
        
    if num < smallest:
        smallest = num
        
print("Largest Number: ", largest)
print("Smallest Number: ", smallest)    
        
        
        
        


# QUESTION 5: Word Frequency Counter
#     1.Ask the user to enter a sentence.
#     2.Convert the sentence into a list of words.
#     3.Use a dictionary to count how many times each word appears.
#     4.Print the word frequency clearly.
# Example Format (for understanding only):
#     apple: 3
#     banana: 2
#     orange: 1
# Requirements:
#      Use string splitting.
#      Use a dictionary for counting.
#      Use loops for processing.


sentence = input("Enter a sentence: ")

Words = sentence.split()            # convert sentence in to a list

Word_frequency = {}                 # empty dictionary

# count each word
for word in Words:
    if word in Word_frequency:
        Word_frequency[word] = Word_frequency[word] + 1
        
    else: 
        Word_frequency[word] = 1
        
print("\nWORD FREQUENCY: ")

for key, value in Word_frequency.items():
    print(key, ":", value)                      # printing word in dictionary







# QUESTION 6: Nested Loops – Multiplication Table
# Using nested loops, print a multiplication table from 1 to 5.
#     Expected Output Format:
#         1 2 3 4 5
#         2 4 6 8 10
#         3 6 9 12 15
#         4 8 12 16 20
#         5 10 15 20 25
# Requirements:
#      Must use nested loops.
#      Proper formatting required.


# Outer Loop
for i in range(1,6):
    # Inner Loop
    for j in range(1,6):
        print(i * j, end=" ")
    
    # inner loop print honay kay baad next line print 
    print()
