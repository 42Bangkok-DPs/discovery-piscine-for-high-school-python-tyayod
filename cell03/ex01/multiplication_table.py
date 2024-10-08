#!/usr/bin/env python3
def main():
    number = int(input("Enter a number: "))

    for i in range(10):
        print(f"{i} x {number} = {i * number}")

main()