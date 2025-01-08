# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose: Your task is to complete the following challenges:
##Create a list of students first names, minimum of 10.
#Print the original list of student names.
#Slice the list to get the first 5 names and print them.
#Slice the list to get the last 3 names and print them.
#Get the size of the list and print it.
#Add a new student name, "Kate", to the end of the list and print the updated list.
#Insert a new student name, "Liam", at index 3 and print the updated list.
#Iterate through the list and print each student name.
# ---------------------------------------------------

#Create a list of students first names, minimum of 10.
student_name =["Vijaya","Saumya","Naisha","Nitya","Akshay","Mansi","Surbhi","Arjun","Aditi","Sai"]

#Print the original list of student names.
print(f"The original list of student names are :\n {student_name}")
print()

#Slice the list to get the first 5 names and print them.
frist_five_student = student_name[:5]
print(f"The list to get the first 5 student Names : \n{frist_five_student}")
print()

#Slice the list to get the last 3 names and print them.
last_three_student = student_name[-3 :]
print(f"The list to get last 3 names : \n{last_three_student}")
print()

#Get the size of the list and print it.
list_size = len(student_name)
print(f"The size of the list are  : {list_size}")

#Add a new student name, "Kate", to the end of the list and print the updated list.
student_name.append("Kate")
print(f"updated list after adding name Kate :  \n {student_name}")
print()

#Insert a new student name, "Liam", at index 3 and print the updated list.
student_name.insert(3,"Liam")
print(f"Insert new student name after at index 3 postion :  \n {student_name}")
print()

#Iterate through the list and print each student name.
print("\nIterating through the list of students:")
for student_name in (student_name):
        print(student_name)
        

#Output
#---------------------------------------------------------------------------------------------
#The original list of student names are :
# ['Vijaya', 'Saumya', 'Naisha', 'Nitya', 'Akshay', 'Mansi', 'Surbhi', 'Arjun', 'Aditi', 'Sai']

#The list to get the first 5 student Names : 
#['Vijaya', 'Saumya', 'Naisha', 'Nitya', 'Akshay']

##The list to get last 3 names : 
#['Arjun', 'Aditi', 'Sai']

#The size of the list are  : 10
#updated list after adding name Kate :
# ['Vijaya', 'Saumya', 'Naisha', 'Nitya', 'Akshay', 'Mansi', 'Surbhi', 'Arjun', 'Aditi', 'Sai', 'Kate']

#Insert new student name after at index 3 postion :
# ['Vijaya', 'Saumya', 'Naisha', 'Liam', 'Nitya', 'Akshay', 'Mansi', 'Surbhi', 'Arjun', 'Aditi', 'Sai', 'Kate']


#Iterating through the list of students:
#Vijaya
#Saumya
#Naisha
#Liam
#Nitya
#Akshay
#Mansi
#Surbhi
#Arjun
#Aditi
#Sai
#Kate
#---------------------------------------------------------------------------------