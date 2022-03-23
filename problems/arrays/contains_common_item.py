def contains_common_item(arr1, arr2):
    ref = {}
    for item in arr1:
        ref[item] = True
    for item in arr2:
        if item in ref:
            return True
    return False

print(contains_common_item(['a', 'b', 'c', 'x'], ['z', 'y', 'i']))
print(contains_common_item(['a', 'b', 'c', 'x'], ['z', 'y', 'x']))
