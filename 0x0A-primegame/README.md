# 0x0A. Prime Game

## Project Overview

The Prime Game is a competitive game played by two players, Maria and Ben. In the game, they take turns picking prime numbers from a list of consecutive integers, starting from 1 up to a given number `n`. When a player picks a prime number, they remove that number and its multiples from the list. The player who cannot make a move loses the game. This project involves creating a function to determine the winner of multiple rounds of the game, given different values of `n` for each round.

### Objectives:
- Implement a function that determines the winner of a Prime Game.
- Optimize the solution using the Sieve of Eratosthenes algorithm for identifying prime numbers.
- Use game theory principles to determine the winner based on optimal play.

## Problem Description

Maria and Ben are playing the Prime Game. Given a set of consecutive integers from 1 to `n`, they take turns choosing a prime number from the set. The player who cannot make a move (i.e., no prime numbers remain for them to choose) loses the game.

### Function Signature:
```python
def isWinner(x, nums):
    pass

