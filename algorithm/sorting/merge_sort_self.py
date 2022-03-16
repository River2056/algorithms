import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[0:middle])
    right = merge_sort(arr[middle:])

    i, j = 0, 0
    new_arr = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_arr.append(left[i])
            i += 1
        elif left[i] > right[j]:
            new_arr.append(right[j])
            j += 1

    while i < len(left):
        new_arr.append(left[i])
        i += 1

    while j < len(right):
        new_arr.append(right[j])
        j += 1

    return new_arr

def main():
    r_start = 1
    r_end = 500
    arr = [random.randint(r_start, r_end) for i in range(r_end)]

    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()

    print('before')
    print(arr)
    print()

    print('after')
    print(sorted_arr)
    print()

    print('time elapsed: ')
    print(f'--- {end_time - start_time} seconds ---')

if __name__ == '__main__':
    main()
