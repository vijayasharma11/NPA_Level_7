# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose:The program should allow users to perform the following operations:
#Add a new student's information.
#Display the list of all students and their information.
#Search for a student by name and display their information.
#Update a student's information.
#Delete a student's information.
#Exit the program.
#Each student's information should be stored in a tuple containing their name, age, and grade. 
#For each operation, provide clear prompts and handle user input appropriately.
# ---------------------------------------------------

#list to create student information
students = []

def add_student():
    name = input("Please Enter student name :")
    age = int(input("Please enter the student age : "))
    grade = input("Please enter the student grade : ")

    #Create a tuple with this information. 
    student = (name,age,grade)

    #add it to the list of students.
    students.append(student)
    print(f"Student {name} has been added successfully.\n")
    
# Function to display all students
def display_students():
    if len(students) == 0:
        print("No students available.\n")
    else:
        print("List of all students:")
        for index, student in enumerate(students, start=1):
            name, age, grade = student
            print(f"{index}. Name: {name}, Age: {age}, Grade: {grade}")
        print()  # Adding a newline for better readability

#Function Searching for a Student by Name
def search_student():
    search_name = input("Please Enter the Name of student? :")
    found = False

    #Iterate through the list of students
    for student in students:
        name,age,grade = student
        if name.lower() == search_name.lower():
            print(f"Student found: Name: {name}, Age: {age}, Grade: {grade}\n")
            found = True
            break
    
    if not found:
        print(f"Student {search_name} not found.\n")

#Function Updating Student Information
def update_student():
    update_name = input("Enter the name of the student to update: ")
    found = False
    
    for i, student in enumerate(students):
        name, age, grade = student
        if name.lower() == update_name.lower():
            new_age = int(input(f"Enter the new age for {name}: "))
            new_grade = input(f"Enter the new grade for {name}: ")
            
            # Update the student's information
            students[i] = (name, new_age, new_grade)
            print(f"Student {name}'s information has been updated successfully.\n")
            found = True
            break
    
    if not found:
        print(f"Student {update_name} not found.\n")

#Deleting Student Information
def delete_student():
    delete_name = ("Please Enter the name of the student to delete: ")
    found = False

    for i, student in enumerate(students):
        if name.lower() == delete_name.lower():
            del students[i]
            print(f"Student {name}'s has been deleted successfully.\n")
            found = True
            break
    
    if not found:
        print(f"Student {delete_name} not found.\n")

#Main function to handle the user function
def main():
    while True:
        print("Chose an options :")
        print("1. Add a new student :")
        print("2. Display all students :")
        print("3. Search for a student :")
        print("4. Update a student's information :")
        print("5. Delete a student's information :")
        print("6. Exit")


        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice =='2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()