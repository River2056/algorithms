def find_factorial_recursive(number, ref={}):
    if number in ref:
        return ref[number]
    if number <= 1:
        return 1
    value = number * find_factorial_recursive(number - 1, ref)
    ref[number] = value
    return value


def find_factorial_iterative(number):
    if number <= 1:
        return 1
    result = 1
    for i in range(result + 1, number + 1):
        result *= i
    return result


def main():
    print("recursive function")
    print(find_factorial_recursive(3))
    print(find_factorial_recursive(5))
    print(find_factorial_recursive(10))
    print(find_factorial_recursive(15))
    print(find_factorial_recursive(20))
    print(find_factorial_recursive(100))
    print()

    print("iterative function")
    print(find_factorial_iterative(3))
    print(find_factorial_iterative(5))
    print(find_factorial_iterative(10))
    print(find_factorial_iterative(15))
    print(find_factorial_iterative(20))
    print(find_factorial_iterative(100))
    print()


if __name__ == "__main__":
    main()
