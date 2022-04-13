import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from common import print_result

def trap_rain_water(height):
    all_filled = [*height]
    stack = []

    for index, block in enumerate(height):
        if block > 0:
            if len(stack) == 0:
                stack.append((index, block))
            elif len(stack) != 0:
                peek_last_block = stack[-1]
                if peek_last_block[1] < block and index - peek_last_block[0] > 1:

            else:
                last_block = stack.pop()
                max_height = min(last_block[1], block)
                if index - last_block[0] > 1:
                    for i in range(last_block[0] + 1, index):
                        all_filled[i] = max_height
                stack.append((index, block))

    
    print(height)
    print(all_filled)

def main():
    print_result([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, trap_rain_water)
    print_result([4, 2, 0, 3, 2, 5], 9, trap_rain_water)

if __name__ == '__main__':
    main()
