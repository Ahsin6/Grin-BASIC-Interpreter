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
LET NAME "Boo" <br/>
LET AGE 13.015625 <br/>
PRINT NAME <br/>
PRINT AGE <br/>
.

Example Output:
Boo <br/>
13.015625

Arithmetic operations:
Example Input:
LET A 4 <br/>
ADD A 3 <br/>
PRINT A <br/>
LET B 5 <br/>
SUB B 3 <br/>
PRINT B <br/>
LET C 6 <br/>
MULT C B <br/>
PRINT C <br/>
LET D 8 <br/>
DIV D 2 <br/>
PRINT D <br/>
.

Example Output:
7 <br/>
2 <br/>
12 <br/>
4 <br/>

Subroutines

There are no functions or methods in Grin, but there is a simplified mechanism called a subroutine. A subroutine is a sequence of Grin statements that can be "called" by executing a GOSUB statement.

Example Input:
LET A 1 <br/>
GOSUB 5 <br/>
PRINT A <br/>
END <br/>
LET A 3 <br/>
RETURN <br/>
PRINT A <br/>
LET A 2 <br/>
GOSUB -4 <br/>
PRINT A <br/>
RETURN <br/>
.

Example Output:
1 <br/>
3 <br/>
3 <br/>




