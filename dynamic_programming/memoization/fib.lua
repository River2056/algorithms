function fib(n, map)
    map = map or {}
    if map[n] ~= nil then
        return map[n]
    end
    if n <= 2 then
        return 1
    end
    value = fib(n - 1, map) + fib(n - 2, map)
    map[n] = value
    return value
end

print(fib(2))
print(fib(8))
print(fib(10))
print(fib(50))
print(fib(100))
print(fib(500))
