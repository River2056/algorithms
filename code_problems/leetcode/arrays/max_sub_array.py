def maxSubArray(nums):
    if len(nums) <= 1:
        return nums[0]
    max_num = nums[0]
    curr = 0
    for i in nums:
        if curr < 0:
            curr = 0
        curr += i
        max_num = max(curr, max_num)
    return max_num


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([-2, 10, 7, -5, 15, 6]))
