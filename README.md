# NIM in Rust
## An implementation for finding a NIM Cycle in Rust given any subtraction sequence

## QUICKSTART
```console
$ rustc nim.rs
$ ./nim
```

## Background of 2-Player 1 String NIM
Nim is a combinarotial two-player game in which each player alternates turns removing any number of tokens from one of possibly many piles.
We will denote the number of tokens that a player can remove on their turn as the subtraction set (a subset of $N$), denoted by $S = {s_1, s_2,...,s_k}$ such that $s_1 < s_2 < ... < s_k$.
