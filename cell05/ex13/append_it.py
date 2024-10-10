#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    for non in sys.argv[1:]:
        if not non.endswith("ism"):
            print(non + "ism")