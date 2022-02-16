def twoSum(nums, target):
    if type(nums) is not list:
        return []
    if len(nums) == 0:
        return []
    ref = {}
    for i, v in enumerate(nums):
        if v in ref:
            return [ref[v], i]
        else:
            diff = target - v
            ref[diff] = i

print(twoSum([2, 7, 11, 15], 9))
