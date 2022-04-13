import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
from common import print_result

def trap_rain_water(height):
    walls = []
    all_filled = []

    start_fill = False
    for index, block in enumerate(height):
        if block > 0 or start_fill:
            start_fill = True
            
        else:
            all_filled.append(block)

    
    print(walls)

def main():
    print_result([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, trap_rain_water)
    print_result([4, 2, 0, 3, 2, 5], 9, trap_rain_water)

if __name__ == '__main__':
    main()
