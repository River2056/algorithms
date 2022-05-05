def fib(n, ref={}):
    if n in ref:
        return ref[n]
    if n <= 2:
        return 1
    value = fib(n - 1, ref) + fib(n - 2, ref)
    ref[n] = value
    return value


print(fib(2))
print(fib(5))
print(fib(8))
print(fib(10))
print(fib(50))
print(fib(100))
print(fib(500))
