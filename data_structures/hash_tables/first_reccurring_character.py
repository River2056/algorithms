"""
    Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    It should return 2
    because 2 is the earliest recurring character

    Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    It should return 1

    Given an array = [2, 3, 4, 5]
    It should return undefined
"""


def first_recurring_character(nums):
    if type(nums) is not list:
        raise Exception("arguments must be list!")
    if len(nums) == 0:
        return None
    ref = {}
    for i, n in enumerate(nums):
        if n in ref:
            return n
        ref[n] = i
    return None


print(first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character([2, 3, 4, 5]))
print(first_recurring_character([]))
print(first_recurring_character("hello"))  # invalid
