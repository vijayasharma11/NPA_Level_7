# Function to get three numbers from the user
def input_numbers():
    num1 = float(input("Enter the first  number : "))
    num2 = float(input("Enter the second number : "))
    num3 = float(input("Enter the Third number : "))
    return num1,num2,num3

#Function to calculate average
def calculate_average(num1,num2,num3):
    sum = num1+num2+num3
    average  = sum/3
    return average

#Function to display average
def display_average(average):
    print (f"The average of the three numbers is: {average }")

#Main Function
def main():
    num1,num2,num3 = input_numbers()
    #calculate average
    average= calculate_average(num1,num2,num3)
    display_average(average)


if __name__ == "__main__":
    main()  

    
