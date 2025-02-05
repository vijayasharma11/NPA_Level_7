# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 22/01/2025
# Purpose: Load a JSON file containing a list of students' information. Each student entry contains name, age, and grades.
#Load the JSON file.
#Calculate the average grade for each student.
#Print the student name, age, grades, and average grade.
#-----------------------------------------------------------------

import json

# Function to calculate the average grade for each student
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Load the students' data from a JSON file
def load_students_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function to process and print the student information
def process_students(file_path):
    students = load_students_data(file_path)
    
    for student in students:
        name = student.get("name")
        age = student.get("age")
        grades = student.get("grades")
        
        # Calculate average grade
        average_grade = calculate_average(grades)
        
        # Print the student details
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Grades: {grades}")
        print(f"Average Grade: {average_grade:.2f}")
        print("-" * 40)

# Run the program
if __name__ == "__main__":
    # Replace with the path to your students.json file
    file_path = r"D:\Vijaya\NPA_Level_7\Exercise_week3b\students.json"
    process_students(file_path)


'''
OUTPUT:

Name: John
Age: 20
Grades: [85, 90, 95]
Average Grade: 90.00
----------------------------------------
Name: Alice
Age: 22
Grades: [80, 75, 85]
Average Grade: 80.00
----------------------------------------
Name: Bob
Age: 21
Grades: [90, 92, 88]
Average Grade: 90.00
----------------------------------------


'''