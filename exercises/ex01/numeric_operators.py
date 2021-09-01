"""Numeric Operators Program"""

__author__ = "730397184"

a: int = int(input("Pick any number: "))

b: int = int(input("Pick another number: "))

print("Left-hand side: " + str(a))

print("Right-hand side: " + str(b))

print(str(a) + " % " + str(b) + " is " + str(a % b))

print(str(a) + "**" + str(b) + " is " + str(a ** b))

print(str(a) + "//" + str(b) + " is " + str(a // b))

print(str(a) + "*" + str(b) + " is " + str(a * b))