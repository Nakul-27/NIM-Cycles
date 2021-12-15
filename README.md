# NIM Cycles
## An implementation for finding a NIM Cycle in Python given any subtraction sequence

## QUICKSTART
```console
$ python3 basic.py
```
## Conjectures Given the Subtraction Set {a,b,c}
~~1. Given c = a + b, then Cl = c + a.~~

~~2. Given c = 2b, and b = 3, then Cl = 9.~~

~~3. Given that safe combinations are being generated, if c = 2b and Cl = 12, then the next Cl = 15.~~

~~4. Given c = 2b, and b = 5, then Cl = 15.~~

~~5. Given c = 2b, and a > 10 and b = 5, then Cl = 15 + (a - 10).~~

~~6. If c = b^2 and a is even and b = 2, then Cl = 6.~~

7. If c = b^2 and a is odd and b = 1, then Cl = 2

## Background of 2-Player 1 String NIM
Nim is a combinatorial two-player game in which each player alternates turns removing any number of tokens from one of possibly many piles.

