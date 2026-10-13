# Stack-Based Mathematical Expression Evaluator

## 1. Project Description

This project is a Python program that reads mathematical expressions from `input.txt`, evaluates them using a stack-based approach, and writes the results to `output.txt`.

## 2. Project Files

- `main.py` — Contains the Stack class and expression evaluation functions.
- `input.txt` — Contains the mathematical expressions to evaluate.
- `output.txt` — Stores the calculated results.

## 3. Requirements

- Python 3 installed on the computer.
- A code editor or terminal to run the program.

## 4. How to Run the Program

1. Place `main.py` and `input.txt` in the same folder.
2. Open a terminal in that folder.
3. Run `python main.py`.
4. Open `output.txt` to view the results.

On Windows, `py main.py` can also be used if necessary.

## 5. Input and Output Format

Each mathematical expression must be written on a separate line in `input.txt`.

The program supports addition (+), subtraction (-), multiplication (*), division (/), parentheses, decimal numbers and negative numbers.

Lines containing only `*`, `---` or `===` are treated as separators and preserved in the output.

## 6. Assumptions and Limitations

- Expressions must contain valid mathematical syntax.
- Division by zero is reported as an error.
- Mismatched parentheses and invalid expressions are reported as errors.
- Exponentiation and other mathematical operators are not supported.
- The input and output files must be accessible in the program's working directory.

## 7. Testing

The program should be tested with expressions involving different operators, parentheses, decimal numbers, negative numbers and division by zero. The output file should be checked to confirm that the results are correct.
