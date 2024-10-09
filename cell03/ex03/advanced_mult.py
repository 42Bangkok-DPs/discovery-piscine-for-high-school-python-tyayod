#!/usr/bin/env python3
def main():
    p = 0

    while p <= 10:
        table = []
        q = 0
        while q <= 10:
            table.append(p*q)
            q = q + 1

        print(f"Table de {p} : {' '.join(map(str, table))}")
        p = p + 1
    

main()


        
