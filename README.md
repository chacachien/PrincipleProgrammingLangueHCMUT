## Bkool Programming Language - Compiler Development

This repository contains the development of a compiler for the Bkool programming language, an object-oriented programming language designed using ANTLR and Python. This Project provides for Principle of Programming Language at HCMUT. 

### Introduction

Bkool is a custom-designed OOP language aiming to offer a robust and user-friendly environment for developers. This project focuses on creating a compiler for Bkool, enabling users to write and execute their code.

### Project Structure

The project is organized into three phases:

1. **Lexer:** (Assignment 1)
   - Defines the lexical structure of the Bkool language.
   - Uses ANTLR to generate a lexer for identifying tokens, keywords, and literals.
2. **Parser:** (Assignment 2)
   - Defines the grammatical structure of Bkool based on the lexer's tokens.
   - Employs ANTLR to create a parser that verifies the syntax of input programs.
3. **AST Generation:** (Assignment 3)
   - Generates an Abstract Syntax Tree (AST) from the parsed program.
   - The AST represents the program's structure in a tree-like format, facilitating further processing, such as code generation or analysis.


### Instructions

1. Install python 3
2. Download and install Java Runtime Environment (can search on youtube)
3. Download antlr version 4.9.2 [at here](https://www.antlr.org/download/antlr-4.9.2-complete.jar),config env var ANTLR_JAR to this path file.
4. Install ANTLR: `pip install antlr4-python3-runtime==4.9.2`
