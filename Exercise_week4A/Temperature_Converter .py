# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 15/01/2025
# Purpose: List Statistics (Lambda Functions).
#-----------------------------------------------------------------

#Create a function convert temperatures that takes a list of Celsius temperatures.
def convert_temperatures(celsius_list): 
    #Define a lambda function fahrenheit(celsius) 
    # that converts Celsius to Fahrenheit (F = (C * 9/5) + 32).
    fahrenheit = lambda celsius : (celsius * 9/5) + 32

    #Convert the entire list of Celsius temperatures to Fahrenheit using map
    fahrenheit_list = list(map(fahrenheit, celsius_list))
    
    # Print the temperatures in Celsius and Fahrenheit
    for celsius, fahrenheit_temp in zip(celsius_list, fahrenheit_list):
        print(f"Celsius: {celsius}°C -> Fahrenheit: {fahrenheit_temp}°F")


celsius_temperatures = [0, 20, 27, 100]
convert_temperatures(celsius_temperatures)

"""
Output:
Celsius: 0°C -> Fahrenheit: 32.0°F
Celsius: 20°C -> Fahrenheit: 68.0°F
Celsius: 27°C -> Fahrenheit: 80.6°F
Celsius: 100°C -> Fahrenheit: 212.0°F
"""