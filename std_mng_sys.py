# student management System

import csv
# Global variables
student_fields = ['name','phone-number', 'date-of-birth', 'Marks-Phy', 'Marks-Chem', 'Marks-Bio', 'Marks-Math']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student information")
    print("2. View Student information")
    print("3. Search a particular Student")
    print("4. Update Student information")
    print("5. Delete Student information")
    print("6. Quit software")


def add_student():
    print("-------------------------")
    print("Add new Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t| ')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    phone = input("phone-number to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if phone == row[1]:
                    print("----- Student Found -----")
                    print("Name: ", row[0])
                    print("phone-number: ", row[1])
                    print("date-of-birth: ", row[2])
                    print("Physics: ", row[3])
                    print("Chemistry: ", row[4])
                    print("Biology: ", row[5])
                    print("Math: ", row[6])
                    break
        else:
            print("Student not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    phone = input("phone-number to search: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if phone == row[1]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Student not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    phone = input("phone-number to search: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if phone != row[1]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student ", phone, "deleted successfully")
    else:
        print("Student not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Have a good day")
print("-------------------------------")