#program to find area and circumference of circle
from math import pi
radius = float(input("Enter radius of a circle"))
print("Area of circle = " + str(pi * radius**2))
print("circumference of circle = " + str(2 * pi * radius))