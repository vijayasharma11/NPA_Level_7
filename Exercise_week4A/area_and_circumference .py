# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 15/01/2025
# Purpose: Area and Circumference Calculator (Functions Returning Multiple Values).
#-----------------------------------------------------------------

import math

#Create a function 
def  calculate_area_circumference(radius):
    #calculate both the area and circumference
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    #return both the value in tuple
    return area, circumference

radius = float(input("Please enter the radius"))
area, circumference = calculate_area_circumference(radius)

#print the result
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

"""
Output :
Please enter the radius 5
Area: 78.54
Circumference: 31.42

 d:/Vijaya/NPA_Level_7/Exercise_week4A/Exercise1.py
Please enter the radius 6.7
Area: 141.03
Circumference: 42.10

"""