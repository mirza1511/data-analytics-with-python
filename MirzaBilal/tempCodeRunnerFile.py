classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
medical_cause = input("Do you have a medical cause? (Y/N): ")

attendance = (classes_attended / classes_held) * 100

print("Attendance percentage:", attendance)

if attendance >= 75 or medical_cause.upper() == "Y":
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")