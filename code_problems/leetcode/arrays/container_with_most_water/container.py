import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent.parent))
from common import print_result

def container_with_most_water(height):
    max_area = 0
    i, j = 0, len(height) - 1
    while i != j:
        w = j - i
        h = min(height[i], height[j])
        area = w * h
        max_area = max(max_area, area)
        
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

def main():
    print_result([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, container_with_most_water)
    print_result([7, 1, 2, 3, 9], 28, container_with_most_water)

if __name__ == '__main__':
    main()
