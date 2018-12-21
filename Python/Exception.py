# Implement a program for square root of a given number by raising and handling an exception if number is negative
import cmath
number = int(input())
# if number > 0:
try:
    print((number)**0.5)
except:
    print("This is a negative root")