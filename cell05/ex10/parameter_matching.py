#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    
    pamt = sys.argv[1]

    input1 = input("What was the parameter?")

    if input1 == pamt:
        print("Good job")
    else :
        print("Nope, sorry...")

main()