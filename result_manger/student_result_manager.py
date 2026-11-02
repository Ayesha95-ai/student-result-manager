student = {}

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add students")
    print("2. View students")
    print("3. Check result of students")
    print("4. Exit")
    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} successfully added!")

    # View student
    elif choice == "2":
        if not student:
            print("Students are not found.")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Check result
    elif choice == "3":
        name = input("Enter student name: ")
        if name in student:
            marks = student[name]

            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found.")

    # Exit
    elif choice == "4":
        print("Exiting....")
        break 

    else:
        print("Invalid input...")