#!/usr/bin/env python3
number = int(input("Enter a number less than 25 : "))

if number >= 25:
    print("Error")
else :
        while True :
            number = number +1
            print("Inside the loop, my variable is ",number)
            if number >= 25:
                 break
    