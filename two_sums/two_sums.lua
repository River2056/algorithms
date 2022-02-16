function twoSum(nums, target)
    if type(nums) ~= 'table' then
        return {}
    end
    if #nums == 0 then
        return {}
    end
    ref = {}
    for i, v in ipairs(nums) do
        if ref[v] ~= nil then
            return {ref[v], i}
        else
            diff = target - v
            ref[diff] = i
        end
    end
end

function printArr(arr)
    s = '['
    for _, v in ipairs(arr) do
        s = s .. v .. ', '
    end
    s = s .. ']'
    print(s)
end

printArr(twoSum({2, 7, 11, 15}, 9))
