def closure_fib():
    cache = {}
    def fib(n):
        if n < 2:
            return n
        if n in cache:
            return cache[n]
        value = fib(n - 1) + fib(n - 2)
        cache[n] = value
        return value
    return fib

def main():
    memo_fib = closure_fib()
    print(memo_fib(3))
    print(memo_fib(5))
    print(memo_fib(6))
    print(memo_fib(7))
    print(memo_fib(20))

if __name__ == '__main__':
    main()
