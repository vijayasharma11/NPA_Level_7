import random

list = [1,2,3,4]

def Modify_list(list):
    list.append(5)

#new_list = [6,7,8]

Modify_list(list)

print(list)

# Original string  
original_string = "Hello World"  
# Applying swapcase() function  
swapped_string = original_string.swapcase()  
# Output  
print("Original string:", original_string)  # Output: Original string: Hello World  
print("Swapped string:", swapped_string)    # Output: Swapped string: hELLO wORLD  


str = "vijaya"
str2 = "sharma"

str2 = str.join(str2)
print(str2)

n = [1,2,3,4,5,6,7]

random.shuffle(n)
print(n)


print(add.__doc__) 

help(add)   