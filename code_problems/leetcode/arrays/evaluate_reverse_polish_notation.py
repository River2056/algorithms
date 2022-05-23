def evalRPN(tokens: list[str]) -> int:
    # operators = ["+", "-", "*", "/"]
    stack = []
    previous = None
    for _, val in enumerate(tokens):
        try:
            number = int(val)
            stack.append(number)
        except ValueError:
            top = stack.pop()
            if not previous:
                previous = top
                top = stack.pop()
            previous = eval(f"{previous}{val if val != '/' else '//'}{top}")
            print(f"{previous}{val if val != '/' else '//'}{top}")

    return previous  # type: ignore


def main():
    # tokens = ["2", "1", "+", "3", "*"]
    # result = evalRPN(tokens)
    # print(result)

    # tokens = ["4", "13", "5", "/", "+"]
    # result = evalRPN(tokens)
    # print(result)

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result = evalRPN(tokens)
    print(result)


if __name__ == "__main__":
    main()
