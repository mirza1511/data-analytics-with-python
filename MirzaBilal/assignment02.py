# Assignment 02 - Python Basics (Conditional Statements)

# 1. Calculate 5% bonus if service is more than 5 years

salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years > 5:
    bonus = salary * 0.05
    print("Net bonus amount:", bonus)
else:
    print("No bonus")



# 2. Check voting eligibility

age = int(input("Enter your age: "))

if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible for voting")



# 3. Check whether number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# 4. Check whether number is divisible by 7

number = int(input("Enter a number: "))

if number % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")
    


# 5. Display Hello if number is a multiple of 5, otherwise Bye

number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Hello")
else:
    print("Bye")



# 6. Calculate electricity bill

units = int(input("Enter number of units: "))

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)

print("Total electricity bill: Rs.", bill)



# 7. Display the last digit of a number

number = int(input("Enter a number: "))

last_digit = number % 10
print("Last digit:", last_digit)



# 9. Check whether rectangle is a square or rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

if length == breadth:
    print("Square")
else:
    print("Rectangle")



# 10. Find the greatest among two integers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest:", num1)
elif num2 > num1:
    print("Greatest:", num2)
else:
    print("Both numbers are equal")



# 11. Calculate total cost with 10% discount

quantity = int(input("Enter quantity: "))

cost_per_unit = 100
total_cost = quantity * cost_per_unit

if quantity > 1000:
    discount = total_cost * 0.10
    final_cost = total_cost - discount
    print("Discount:", discount)
    print("Total cost after discount:", final_cost)
else:
    print("Total cost:", total_cost)
    


# 12. Grade according to marks

marks = float(input("Enter marks: "))

if marks < 25:
    print("Grade: F")
elif marks <= 45:
    print("Grade: E")
elif marks <= 50:
    print("Grade: D")
elif marks <= 60:
    print("Grade: C")
elif marks <= 80:
    print("Grade: B")
else:
    print("Grade: A")



# 13. Find oldest and youngest among three people

age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))

if age1 >= age2 and age1 >= age3:
    oldest = age1
elif age2 >= age1 and age2 >= age3:
    oldest = age2
else:
    oldest = age3

if age1 <= age2 and age1 <= age3:
    youngest = age1
elif age2 <= age1 and age2 <= age3:
    youngest = age2
else:
    youngest = age3

print("Oldest age:", oldest)
print("Youngest age:", youngest)



# 14. Check exam eligibility based on attendance

classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance = (classes_attended / classes_held) * 100

print("Attendance percentage:", attendance)

if attendance >= 75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")
    
    

# 15. Attendance with medical cause

classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
medical_cause = input("Do you have a medical cause? (Y/N): ")

attendance = (classes_attended / classes_held) * 100

print("Attendance percentage:", attendance)

if attendance >= 75 or medical_cause.upper() == "Y":
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")
    
    

# 16. Check leap year

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")



# 17. Determine place of service

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
marital_status = input("Enter marital status (Y/N): ").upper()

if gender == "F":
    print("Employee will work in urban areas only")

elif gender == "M":
    if 20 <= age < 40:
        print("Employee may work anywhere")
    elif 40 <= age <= 60:
        print("Employee will work in urban areas only")
    else:
        print("ERROR")

else:
    print("ERROR")


