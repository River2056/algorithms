def decode_string(s: str) -> str:
    stack = []
    decoded_string = []

    for letter in s:
        if letter != "]":
            stack.append(letter)
        else:
            # letter == "]"
            while True:
                elem = stack.pop()
                if elem != "[":
                    decoded_string.append(elem)
                else:
                    break

            # get number
            repeated_times = []
            while len(stack) > 0 and stack[-1].isdigit():
                repeated_times.insert(0, stack.pop())

            ds = int("".join(repeated_times)) * "".join(decoded_string)

            # push back to stack backwards
            for e in range(len(ds) - 1, -1, -1):
                stack.append(ds[e])
            decoded_string.clear()

    return "".join(stack)


def test(s: str):
    res = decode_string(s)
    print(res)


def main():
    test("3[a]2[bc]")
    test("3[a2[c]]")
    test("2[abc]3[cd]ef")
    test("100[leetcode]")


if __name__ == "__main__":
    main()
