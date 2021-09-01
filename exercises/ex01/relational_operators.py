"""Relational Operators Program"""

__author__ = "730397184"

a: int = int(input("Pick any number: "))

b: int = int(input("Pick another number: "))

print("Left-hand side:" + str(a))

print("right-hand side:" + str(b))

print(str(a) + ">" + str(b) + " is " + str(bool(a > b)))

print(str(a) + "==" + str(b) + " is " + str(bool(a == b)))

print(str(a) + "!=" + str(b) + " is " + str(bool(a != b)))

print(str(a) + "<=" + str(b) + " is " + str(bool(a <= b)))