class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create an object of each class
dog = Dog()
cat = Cat()

# Call the make_sound() method for each object
dog.make_sound()  # Output: Woof! Woof!
cat.make_sound()  # Output: Meow!
