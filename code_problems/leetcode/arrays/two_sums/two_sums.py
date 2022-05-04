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

def main():
    indices = twoSum([2, 7, 11, 15], 9)
    print('indices: ', indices)
    assert indices == [0, 1], f'should be [0, 1], got {indices} instead'

if __name__ == '__main__':
    main()
