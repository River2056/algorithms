def merge_sorted_array(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise Exception("Please pass in list type parameters!")
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr2[j] <= arr1[i]:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


print(merge_sorted_array([0, 15, 22, 31], [1, 3, 11, 47]))
print(merge_sorted_array([20, 23, 75, 88], [90, 99]))
print(merge_sorted_array([], [20, 30, 40]))
print(merge_sorted_array([1], [20, 30, 40]))
print(merge_sorted_array("hello", "world"))  # invalid
