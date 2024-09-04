# Grin-BASIC-Interpreter

Project Overview

This project involves building an interpreter for a simplified version of the BASIC programming language called Grin. Grin supports basic operations such as variable assignments, arithmetic, and flow control. Task is to create a Python-based interpreter that can read Grin programs, execute them, and produce output.

Project Structure

The project is structured into multiple modules for different functionalities:

project3.py: The main module that runs the Grin interpreter.
grin package: Contains modules that handle lexing, parsing, and executing Grin programs.
tests/grin: Contains unit tests for the Grin interpreter modules.
Input Program Structure

Grin programs consist of statements, one per line, and are terminated by a period (.) as an end-of-program marker. Each statement can include:

LET: Assign a value to a variable.
PRINT: Print a variable's value.
INNUM / INSTR: Read a number or string from input.
ADD, SUB, MULT, DIV: Perform arithmetic operations.
GOTO / GOSUB: Jump to a specific line or subroutine.
RETURN: Return from a subroutine.
END: End the program.

# Dont copy paste the input! Enter each line individually!
Example Input:
LET NAME "Boo" /n
LET AGE 13.015625 /n
PRINT NAME /n
PRINT AGE /n
.

Example Output:
Boo
13.015625

Arithmetic operations:
Example Input:
LET A 4
ADD A 3
PRINT A
LET B 5
SUB B 3
PRINT B
LET C 6
MULT C B
PRINT C
LET D 8
DIV D 2
PRINT D
.

Example Output:
7
2
12
4

Subroutines

There are no functions or methods in Grin, but there is a simplified mechanism called a subroutine. A subroutine is a sequence of Grin statements that can be "called" by executing a GOSUB statement.

Example Input:
LET A 1
GOSUB 5
PRINT A
END
LET A 3
RETURN
PRINT A
LET A 2
GOSUB -4
PRINT A
RETURN
.

Example Output:
1
3
3




