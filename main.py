
import re


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def tokenize(expression):
    pattern = r"\d+(?:\.\d+)?|[+\-*/()]"
    tokens = re.findall(pattern, expression)
    if "".join(tokens).replace(" ", "") != expression.replace(" ", ""):
        raise ValueError("Invalid character in expression")
    return tokens


def to_postfix(expression):
    tokens = tokenize(expression)
    operators = Stack()
    output = []

    precedence = {
        "+": 1, "-": 1,
        "*": 2, "/": 2,
        "u+": 3, "u-": 3
    }

    previous = None

    for token in tokens:
        if re.fullmatch(r"\d+(?:\.\d+)?", token):
            output.append(token)

        elif token in ("+", "-") and (
            previous is None or previous in ("+", "-", "*", "/", "(", "u+", "u-")
        ):
            operators.push("u" + token)

        elif token in precedence:
            while not operators.is_empty() and operators.peek() != "(":
                top = operators.peek()
                if precedence.get(top, 0) >= precedence[token]:
                    output.append(operators.pop())
                else:
                    break
            operators.push(token)

        elif token == "(":
            operators.push(token)

        elif token == ")":
            while not operators.is_empty() and operators.peek() != "(":
                output.append(operators.pop())

            if operators.is_empty():
                raise ValueError("Mismatched parentheses")

            operators.pop()

        previous = token

    while not operators.is_empty():
        top = operators.pop()
        if top == "(":
            raise ValueError("Mismatched parentheses")
        output.append(top)

    return output


def evaluate_expression(expression):
    postfix = to_postfix(expression)
    values = Stack()

    for token in postfix:
        if re.fullmatch(r"\d+(?:\.\d+)?", token):
            values.push(float(token))

        elif token in ("u+", "u-"):
            number = values.pop()
            values.push(number if token == "u+" else -number)

        else:
            right = values.pop()
            left = values.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                if right == 0:
                    raise ValueError("Division by zero")
                result = left / right
            else:
                raise ValueError("Unknown operator")

            values.push(result)

    if values.is_empty():
        raise ValueError("Empty expression")

    result = values.pop()

    if not values.is_empty():
        raise ValueError("Invalid expression")

    if result.is_integer():
        return str(int(result))

    return str(result)


def process_file():
    separators = {"*", "---", "==="}

    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    results = []

    for line in lines:
        expression = line.strip()

        if not expression:
            results.append("")
        elif expression in separators:
            results.append(expression)
        else:
            try:
                results.append(evaluate_expression(expression))
            except (ValueError, IndexError) as error:
                results.append(f"Error: {error}")

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(results))

    print("Evaluation complete. Results saved in output.txt.")


if __name__ == "__main__":
    process_file()
