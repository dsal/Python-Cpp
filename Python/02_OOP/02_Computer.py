class Computer:
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu

class Laptop(Computer):
    pass

class Laptop_size(Computer):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size



# TESTING:
pc1 = Computer(4, 6, 4)
print(pc1.value())

laptop1 = Laptop(16, 2, 5)
print(laptop1.value())

Laptop_size.size = 15
laptop2 = Laptop_size(16, 2, 5)
print(laptop2.value())



""""
This program demonstrates key concepts of OOP:
- Encapsulation: attributes and methods bound together in the Computer (class).
- Inheritance: Laptop and Laptop_size reuse functionality from the Computer (class).
- Polymorphism (method overriding): Laptop_size redefines value() to change behavior.

Class vs. Instance Attributes:
Laptop_size.size is defined as a class attribute,
while ram, hard, and cpu are instance attributes.
"""