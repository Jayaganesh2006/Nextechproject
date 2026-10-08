import csv

search_name = input("Enter student name: ")

found = False

with open("students.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    print("\nStudents Found:")
    print("----------------------------------------")

    for student in reader:

        if student["Name"].lower() == search_name.lower():

            print(
                student["RegisterNo"], "|",
                student["Name"], "|",
                student["Department"], "|",
                student["Year"]
            )

            found = True

if not found:
    print("Student not found.")

