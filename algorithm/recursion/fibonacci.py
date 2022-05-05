def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    if n < 2:
        return n
    else:
        pre2_val = 0
        pre1_val = 1
        curr = 0
        for i in range(2, n + 1):
            curr = pre2_val + pre1_val
            pre2_val = pre1_val
            pre1_val = curr
        return curr


def main():
    print("recursive")
    print(fib_recursive(10))
    print()

    print("iterative")
    print(fib_iterative(10))


if __name__ == "__main__":
    main()
