import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from common import print_result

def trap_rain_water_brute_force(height):
    # count every units of water for each element
    total_amount = 0
    for index, block in enumerate(height):
        left_max = max(height[0:index]) if len(height[0:index]) > 0 else 0
        right_max = max(height[index+1:]) if len(height[index+1:]) > 0 else 0
        amount = min(left_max, right_max) - block
        if amount <= 0:
            continue
        total_amount += amount
    return total_amount

def trap_rain_water(height):
    total_amount = 0
    pl = 0
    pr = len(height) - 1
    max_left = 0
    max_right = 0
    while pl < pr:
        current = height[pl]
        max_left = max(height[pl], max_left)
        max_right = max(max_right, height[pr])
        amount = min(max_left, max_right) - current
        total_amount += amount if amount >= 0 else 0

        if height[pl] < height[pr]:
            pl += 1
        else:
            pr -= 1
    return total_amount

def main():
    print_result([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, trap_rain_water_brute_force)
    print_result([4, 2, 0, 3, 2, 5], 9, trap_rain_water_brute_force)

    print_result([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, trap_rain_water)
    print_result([4, 2, 0, 3, 2, 5], 9, trap_rain_water)

if __name__ == '__main__':
    main()
