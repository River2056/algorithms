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
    # import custom print function
    import os, sys
    from pathlib import Path
    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
    from common import print_sort_result_benchmark

    print_sort_result_benchmark(1, 100, merge_sort)

if __name__ == '__main__':
    main()
