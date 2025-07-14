
# Prototype interface

from abc import ABC, abstractmethod
from copy import deepcopy

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def clone(self):
        pass

#Concrete interface

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Circle(Color: {self.color}, Radius: {self.radius})"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Rectangle(Color: {self.color}, Width: {self.width}, Height: {self.height})"


#USAGE:

# Original shapes
original_circle = Circle("Red", 10)
original_rectangle = Rectangle("Blue", 20, 30)

print("Original Shapes:")
print(original_circle)
print(original_rectangle, "\n")

# Cloned shapes with slight modifications
cloned_circle = original_circle.clone()
cloned_circle.color = "Green"  # Changing color of cloned circle

cloned_rectangle = original_rectangle.clone()
cloned_rectangle.width = 25  # Changing width of cloned rectangle

print("Cloned and Modified Shapes:")
print(cloned_circle)
print(cloned_rectangle)
