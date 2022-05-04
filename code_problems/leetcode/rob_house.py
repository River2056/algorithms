def rob_house(nums):
    """
        You are a professional robber planning 
        to rob houses along a street. Each 
        house has a certain amount of money 
        stashed, the only constraint stopping 
        you from robbing each of them is that 
        adjacent houses have security systems 
        connected and it will automatically 
        contact the police if two adjacent 
        houses were broken into on the same 
        night.

        Given an integer array nums 
        representing the amount of money 
        of each house, return the maximum 
        amount of money you can rob tonight 
        without alerting the police.
    """
    if len(nums) <= 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max([nums[0], nums[1]])
    dp = []
    # 0
    dp.append(nums[0])
    # 1
    dp.append(max([nums[0], nums[1]]))

    # 2~
    # starting from 3 houses,
    # the choice will be either
    # the current + previous two
    # or the previous one
    for i in range(2, len(nums)):
        dp.append(max([nums[i] + dp[i-2], dp[i-1]]))
    return dp[len(nums)-1]

def main():
    result1 = rob_house([1, 2, 3, 1])
    print('result1: ', result1)
    assert result1 == 4, f'should be 4, got {result1} instead'

    result2 = rob_house([2, 7, 9, 3, 1])
    print('result2: ', result2)
    assert result2 == 12, f'should be 12, got {result2} instead'

    result3 = rob_house([2, 1, 1, 2])
    print('result3: ', result3)
    assert result3 == 4, f'should be 4, got {result3} instead'

    result4 = rob_house([1, 2, 1, 1])
    print('result4: ', result4)
    assert result4 == 3, f'should be 3, got {result4} instead'

if __name__ == '__main__':
    main()
