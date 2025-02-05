class Dog:
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute
    def bark(self):  # Method
        print(f"{self.name} says Woof!")
# Creating an instance of the class
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Accessing an attribute # Buddy
my_dog.bark()  # Calling a method Buddy says Woof!
