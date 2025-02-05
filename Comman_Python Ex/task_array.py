import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])

#Accessing Elements
print(arr[0])  # Output: 1
print(arr[-1])  # Output: 5

#Adding Elements
arr.append(6)
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])

#Extend with multiple elements:
arr.extend([7, 8])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8])

#Inserting Elements
arr.insert(2, 10)  # Insert 10 at index 2
print(arr)  # Output: array('i', [1, 2, 10, 3, 4, 5])

#Removing Elements
arr.remove(3)
print(arr)  # Output: array('i', [1, 2, 10, 4, 5])

#Pop an element by index:
arr.pop(1)
print(arr)  # Output: array('i', [1, 10, 4, 5])

#Slicing
sliced = arr[1:4]
print(sliced)  # Output: array('i', [10, 4, 5])

#Searching
index = arr.index(10)  # Find the index of 10
print(index)  # Output: 1

#Reversing
arr.reverse()
print(arr)  # Output: array('i', [5, 4, 10, 1])

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

# Creating objects (instances of the class)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing attributes and methods of objects
print(car1.brand)  # Output: Toyota
car1.start()  # Output: Toyota Corolla is starting.

print(car2.brand)  # Output: Honda
car2.start()  # Output: Honda Civic is starting.
