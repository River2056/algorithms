twice = lambda x: print(x)


def foo(y):
    return lambda x: print(f"x: {x}, y: {y}")


twice(2)

twice(foo(3)(5))
