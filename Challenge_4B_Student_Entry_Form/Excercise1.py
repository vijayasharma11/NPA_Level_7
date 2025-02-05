# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 22/01/2025
# Purpose:you will create a Python program that allows the user to enter data for college students. 
# The program will include functions, lambda functions, input validation, 
# and the ability to pass multiple values to functions.
#-----------------------------------------------------------------
# Lambda functions for validation
validate_age = lambda age: isinstance(age, int) and 16 <= age <= 100
validate_name_length = lambda name: len(name) > 0 and len(name) < 50
validate_presence = lambda name: len(name) > 0
validate_type = lambda name: name.isalnum()

# Function to get student data
def get_student_data():
    # Prompting user for student data and validating inputs
    while True:
        first_name = input("Enter First Name (Alphanumeric, less than 50 characters): ")
        if not validate_name_length(first_name):
            print("Error: First name must be non-empty and less than 50 characters.")
            continue
        if not validate_type(first_name):
            print("Error: First name should contain only alphanumeric characters.")
            continue
        if not validate_presence(first_name):
            print("Error: First name cannot be empty.")
            continue
        
        # Validate age input
        while True:
            try:
                age = int(input("Enter Age (Between 16 and 100): "))
                if validate_age(age):
                    break
                else:
                    print("Error: Age must be between 16 and 100.")
            except ValueError:
                print("Error: Age must be an integer.")
        
        # Validate field of study input
        while True:
            field_of_study = input("Enter Field of Study (Alphanumeric, less than 50 characters): ")
            if not validate_name_length(field_of_study):
                print("Error: Field of study must be non-empty and less than 50 characters.")
                continue
            if not validate_type(field_of_study):
                print("Error: Field of study should contain only alphanumeric characters.")
                continue
            if not validate_presence(field_of_study):
                print("Error: Field of study cannot be empty.")
                continue
            break
        
        # Return collected and validated data as a tuple
        return (first_name, age, field_of_study)

# Main program
def main():
    students = []
    
    while True:
        print("\nEnter student data:")
        student_data = get_student_data()
        students.append(student_data)
        print("Student data recorded successfully!")
        
        # Ask if user wants to continue
        continue_input = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break
    
    # Print summary of entered data
    print("\nSummary of entered student data:")
    print(f"Total students entered: {len(students)}")
    for student in students:
        first_name, age, field_of_study = student
        print(f"Name: {first_name}, Age: {age}, Field of Study: {field_of_study}")

if __name__ == "__main__":
    main()


'''
Output:

Enter student data:
Enter First Name (Alphanumeric, less than 50 characters): Jhon
Enter Age (Between 16 and 100): 24
Enter Field of Study (Alphanumeric, less than 50 characters): Engineering
Student data recorded successfully!
Do you want to enter another student? (yes/no): no

Summary of entered student data:
Total students entered: 1
Name: Jhon, Age: 24, Field of Study: Engineering

'''