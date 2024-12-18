# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 18/12/2024
# Purpose:Create two sets set1 and set2 containing integers. Find and print the union of these two sets.
# Find and print the intersection of set1 and set2.
# Create a set named my_set with the following elements: {'apple', 'banana', 'orange', 'banana', 'kiwi'}. Print the length of the set and observe the output.
#  Write a function that takes two sets as input and returns a new set containing only the elements that are common to both input sets.
# Create a set named vowels containing all the vowels in the English alphabet. Create another set named word containing the letters in the word 'hello'. Find and print the vowels present in the word.in the tuple.
# ---------------------------------------------------

#Create two sets set1 and set2 containing integers
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

#print the union of these two sets.
union_set =set1.union(set2)
print(f"Union of set1 and set2 : {union_set}")
print()

#find the intersection of set1 and set2.
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2 : {intersection_set}")
print()

#Create a set named my_set
my_set = {'apple', 'banana', 'orange', 'banana', 'kiwi'}
# Print the length of the set
print("Length of my_set:", len(my_set))
print()

#Write a function that takes two sets as input and returns a new set 
# containing only the elements that are common to both input sets.

def find_commom_elements(set1,set2):
    return set1.intersection(set2)

a = {1, 2, 3, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8}

common_elecments = find_commom_elements(a , b)
print("Common elements between a and b:", common_elecments)
print()

#Create a set named vowels containing all the vowels in the English alphabet
vowels = {'a','e','i','o','u'}

#Create another set named word containing the letters in the word 'hello'.
word = set('hello')
vowels_in_word = vowels.intersection(word)
print("Vowels in the word 'hello':", vowels_in_word)




#-------------------------------------------------------------------------
#output:
#Union of set1 and set2 : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#Intersection of set1 and set2 : set()

#Length of my_set: 4

#Common elements between a and b: {3, 4, 5, 6}

#"Vowels in the word 'hello':", {'e', 'o'}
#------------------------------------------------------------------------------------