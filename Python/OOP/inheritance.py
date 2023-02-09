import math
class Quadrangle:
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def circumference(self):
        return self.a + self.b + self.c + self.d


class Parallelogram(Quadrangle):
    def __init__(self, name, a, b, alpha):
        self.name = name
        self.a = a
        self.b = b
        self.alpha = alpha

    def circumference(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b * math.sin(math.radians(self.alpha))


class Rectangle(Parallelogram):
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Parallelogram):
    def __init__(self, name, a):
        self.name = name
        self.a = a
        self.b = a

    def circumference(self):
        return 4 * self.a

    def area(self):
        return self.a * self.a

h1 = Rectangle("h1", 5, 6)
print(h1.name)
print(h1.a)                 
print(h1.circumference())   # Parallelogram circumference
print(h1.area())    # own area
print(h1.d)         # AttributeError: 'Rectangle' object has no attribute 'd'





