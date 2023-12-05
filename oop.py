class Dog:
    def __init__(self, name, breed, age):  # Constructor
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"Woof! Woof! My name is {self.name} and I am a {self.breed} dog!")

# Create an object of the Dog class
dog1 = Dog('Max', 'Labrador Retriever', 5)
dog2 = Dog('Charlie', 'Golden Retriever', 3)

# Make the dogs bark
dog1.bark()
dog2.bark()