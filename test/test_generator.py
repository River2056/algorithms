def fib_generator():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def main():
    result = fib_generator()

    for i in range(100):
        val = next(result)
        if i == 0:
            print(val)

if __name__ == '__main__':
    main()
