function merge_sorted_array(arr1, arr2)
    if type(arr1) ~= 'table' or type(arr2) ~= 'table' then
        error('arguments must be arrays!')
    end
    if #arr1 == 0 then
        return arr2
    end
    if #arr2 == 0 then
        return arr1
    end
    i, j = 1, 1
    result = {}
    
    while (i <= #arr1 and j <= #arr2) do
        if arr1[i] <= arr2[j] then
            table.insert(result, arr1[i])
            i = i + 1
        elseif arr2[j] <= arr1[i] then
            table.insert(result, arr2[j])
            j = j + 1
        end
    end

    while (arr1[i] ~= nil) do
        table.insert(result, arr1[i])
        i = i + 1
    end

    while (arr2[j] ~= nil) do
        table.insert(result, arr2[j])
        j = j + 1
    end

    return result
end

-- helper print function
function printArray(arr)
    s = '['
    for _, v in ipairs(arr) do
        s = s .. tostring(v) .. ','
    end
    s = s .. ']'
    print(s)
end

printArray(merge_sorted_array({0, 15, 22, 31}, {1, 3, 11, 47}))
printArray(merge_sorted_array({20, 23, 75, 88}, {90, 99}))
printArray(merge_sorted_array({1}, {10, 20, 30}))
printArray(merge_sorted_array({}, {11, 27, 30}))
printArray(merge_sorted_array('hello')) -- invalid
