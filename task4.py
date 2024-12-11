str1 = "Hello"
str2 = "World"

result = str1 + " " + str2

print(result)  # Output: "Hello World"

text = "  Python Programming  "
#String Length
length = len(text)
print("Length of the string:", length)

#Accessing Characters
first_char = text[0]  # Access the first character (P)
second_char = text[1]  # Access the second character (y)

print("First character:", first_char)
print("Second character:", second_char)

#Slicing - Extracting a portion of a string (substring).

substring = text[5 : 18]
print("substring : ", substring)

#String Methods - Using built-in string methods for various operations.
name = "   Python Programming   "
# Remove leading and trailing whitespace
trimmed_text = name.strip()
print("Trimed_text : ",trimmed_text)

upper_case_name = text.upper()
print(upper_case_name)

# Replace a substring
new_text  = text.replace("Programming","Language")
print(new_text)

#String Formatting - Using string formatting to insert values into a string.
name = "Vijaya"
age = 30

formatted_text = (f"My Name is {name} and I am {age} year old.")
print(formatted_text)

#Splitting - Splitting a string into a list of substrings based on a delimiter.
text ="apple, banana,cherry"
fruits = text.split(",")
print(fruits)

#Checking Substrings - Checking if a string contains a specific substring.
text = "Python Programming"

contains_python = "Python" in text
print("Contains 'Python':", contains_python)

my_list = [1,2,3,4,5,6,7]

if 8 in my_list :
    print("Value 8 is in the list")
else :
    print("Value 8 is not in the list")

my_dict ={'a': 1, 'b':2}
if 'b'in my_dict:
    print("key b in my dictonary")
else :
    print("Key b is not in dictonary")    


