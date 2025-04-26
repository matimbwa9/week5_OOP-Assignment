# Animal class definition (Base class)
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method!")

# Dog class (Inheritance)
class Dog(Animal):
    def move(self):
        return "The dog is running 🐕"

# Cat class (Inheritance)
class Cat(Animal):
    def move(self):
        return "The cat is walking gracefully 🐈"

# Bird class (Inheritance)
class Bird(Animal):
    def move(self):
        return "The bird is flying 🦅"

# Creating objects of the Animal subclasses
dog = Dog()
cat = Cat()
bird = Bird()

# Calling move() method on each object
print(dog.move())
print(cat.move())
print(bird.move())
