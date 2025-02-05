class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Output: Woof (from Dog), Meow (from Cat)


x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)  # True (values are the same)
print(x is y)  # False (they are different objects in memory)
print(z is x)

s = "Hell World!"
modified_s = s[:4] + "," + s[4:]
print(modified_s)


s = "apple,banana,orange"
print(s.split(","))  
