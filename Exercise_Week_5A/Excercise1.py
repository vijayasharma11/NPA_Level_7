# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose:Write a Python function to perform a linear search in a list. 
# The function should take two parameters: 
# the list to search through and the target value to search for. 
# It should return the index of the target value if found, 
# or -1 if the target value is not in the list.
# ---------------------------------------------------
# Exercise 1 - Linear Search
def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Exercise 2 - Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap if the element found is greater than the next element
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Exercise 3 - Combined Exercise
def combined_exercise():
    # Prompt user for a list of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    user_list = list(map(int, user_input.split()))
    
    # Ask for the target value
    target = int(input("Enter the target value to search for: "))
    
    # Perform linear search
    index = linear_search(user_list, target)
    print(f"Index of target value ({target}): {index}")
    
    # Sort the list using bubble sort
    sorted_list = bubble_sort(user_list)
    print(f"Sorted list: {sorted_list}")

# Run the combined exercise
combined_exercise()

'''
OUTPUT:
Enter a list of integers separated by spaces: 3 1 4 1 5 9 2
Enter the target value to search for: 5
Index of target value (5): 4
Sorted list: [1, 1, 2, 3, 4, 5, 9]
PS D:\Vijaya\NPA_Level_7> 
'''