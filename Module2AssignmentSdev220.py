# Noah Beach
# File name is Module2AssignmentSdev220.py
# My app will determine if a student is on the honor roll and/or Dean's list based on their GPA
while True:
    last_name = input("Enter your last name: ")
    if last_name == "ZZZ":
        print("Stopping Program")
        break
    first_name = input("Enter your first name: ")
    gpa = float(input("Enter your GPA: "))
    if gpa >= 3.5:
        print("You have made the Dean's List!")
    if gpa >= 3.25:
        print("You have made Honor Roll!")