# 0x05. N Queens

## Project Overview

The N-Queens problem is a classic puzzle in computer science and mathematics that challenges you to place **N non-attacking queens** on an **N×N chessboard**. The task requires using a **backtracking algorithm** to find all possible solutions. This project will help you learn and practice key concepts in algorithms, recursion, and Python programming.

## Concepts Learned

### 1. **Backtracking Algorithms**

Backtracking is a powerful algorithmic technique used to solve problems incrementally, trying partial solutions and abandoning them if they lead to an invalid or incomplete solution.

- **Definition**: Backtracking is a method of solving problems by exploring all possible solutions and "backtracking" when a solution is not valid.
- **Application to N-Queens**: The N-Queens problem is solved by trying to place queens one by one on the board. For each queen, we attempt to place it in a valid column of the current row. If placing the queen leads to a conflict later on, we backtrack by removing the queen and trying a different column.

This project teaches you how to design and implement a backtracking algorithm to explore all possible configurations and find solutions efficiently.

### 2. **Recursion**

Recursion is a method in programming where a function calls itself to solve smaller instances of a problem.

- **Recursive Backtracking**: In this project, recursion is used to place queens row by row. Each recursive call tries to place a queen in a row and proceeds to the next row, until all rows are filled.
- **Base Case**: The recursion halts when all queens are placed, and a solution is found.
- **Recursive Calls**: If placing a queen doesn't lead to a solution, the function backtracks to the previous row and tries placing the queen in a different column.

Through recursion, you will learn how problems can be broken down into simpler sub-problems that can be solved in a repetitive manner.

### 3. **List Manipulations in Python**

Lists are a fundamental data structure in Python, and this project requires you to manipulate lists to represent the chessboard and store the positions of the queens.

- **Storing Queen Positions**: The board is represented by a list where each index corresponds to a row on the chessboard, and the value at that index represents the column where a queen is placed.
- **Backtracking with Lists**: As part of the backtracking process, the list is modified to add and remove queens as needed, simulating placing and removing queens on the board.

This project will help you practice working with lists and using them to store and manipulate information in a structured way.

### 4. **Python Command-Line Arguments**

Command-line arguments are used to pass input parameters to Python scripts when executing them from the terminal.

- **Handling Input**: In this project, you will handle command-line arguments to read the value of `N` (the size of the chessboard). The program must ensure that the input is a valid integer and that `N` is greater than or equal to 4.
- **Error Handling**: The script will handle various types of input errors, such as incorrect number of arguments or non-integer values, and print appropriate error messages.

By working with command-line arguments, you will gain experience in reading and validating user input in a Python script.

### 5. **PEP 8 Code Style**

PEP 8 is the official style guide for Python code, and following it ensures that your code is clean, readable, and maintainable.

- **Indentation**: Using 4 spaces per indentation level.
- **Function and Variable Naming**: Using lowercase letters with underscores for function and variable names (snake_case).
- **Documentation**: Writing clear docstrings to explain the purpose of functions and their parameters.

This project will help you practice writing PEP 8-compliant Python code, which is crucial for writing professional and maintainable code.

## How to Run the Program

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/alx-interview.git

