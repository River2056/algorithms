def evalRPN_self(tokens: list[str]) -> int:
    stack = []
    for _, val in enumerate(tokens):
        try:
            number = int(val)
            stack.append(number)
        except ValueError:
            previous = stack.pop()
            top = stack.pop()
            res = int(eval(f"{top}{val}{previous}"))
            stack.append(res)

    return stack.pop()  # type: ignore


def evalRPN(tokens: list[str]) -> int:
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),
    }
    stack = []

    for _, val in enumerate(tokens):
        if val in operators:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            res = operators[val](num2, num1)
            stack.append(res)
        else:
            stack.append(val)

    return stack.pop()


def main():
    tokens = ["12", "7", "-"]
    result = evalRPN(tokens)
    print(result)

    tokens = ["2", "1", "+", "3", "*"]
    result = evalRPN(tokens)
    print(result)

    tokens = ["4", "13", "5", "/", "+"]
    result = evalRPN(tokens)
    print(result)

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result = evalRPN(tokens)
    print(result)


if __name__ == "__main__":
    main()
