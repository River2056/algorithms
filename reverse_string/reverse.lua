function reverse(str)
    result = ''
    for i = #str, 1, -1 do
        result = result .. str:sub(i, i)
    end
    return result
end

print(reverse('hello'))
