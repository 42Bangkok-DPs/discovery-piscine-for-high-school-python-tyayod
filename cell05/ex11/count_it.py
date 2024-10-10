#!/usr/bin/env python3
import sys

def main():
    parameters = sys.argv[1:]

    if not parameters:
        print("none")
    else:
        print(f"parameters: {len(parameters)}")
        
        for param in parameters:
            print(f"{param}: {len(param)}")
main()