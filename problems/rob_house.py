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
    odd = 0
    even = 0
    for i, v in enumerate(nums):
        if i % 2 == 0:
            even += v
        else:
            odd += v
    return max([odd, even])

def main():
    result1 = rob_house([1, 2, 3, 1])
    print('result1: ', result1)
    assert result1 == 4, f'should be 4, got {result1} instead'

    result2 = rob_house([2, 7, 9, 3, 1])
    print('result2: ', result2)
    assert result2 == 12, f'should be 12, got {result2} instead'

if __name__ == '__main__':
    main()
