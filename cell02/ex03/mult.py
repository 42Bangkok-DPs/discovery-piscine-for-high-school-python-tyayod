#!/usr/bin/env python3
first = int(input("Enter the first number : "))
second = int(input("Enter the second number : "))
multi = first*second

if multi >0 :
    print(first, "x" , second,"=",multi)
    print("The result is positive")

elif multi == 0 :
    print(first, "x" , second,"=",multi)
    print("The result is positive and negative")

else :
    print(first, "x" , second,"=",multi)
    print("The result is negative")
