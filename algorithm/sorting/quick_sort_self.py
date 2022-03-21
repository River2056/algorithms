def quick_sort(array):
    if len(array) <= 1:
        return array
    arr = [val for val in array]
    print('arr: ', arr)
    pivot = arr[-1]
    i, j = -1, 0
    for e in range(len(arr)):
        if e == len(arr) - 1:
            i += 1
            tmp = arr[i]
            arr[i] = pivot
            arr[e] = tmp
        if arr[e] < pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        j += 1
    print('i, j: ', i, j)
    left = quick_sort(arr[0:i])
    print('left: ', left)
    right = quick_sort(arr[i:])
    print('right: ', right)
    return left + right

def main():
    # import custom print function
    import os, sys
    from pathlib import Path
    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
    from common import print_sort_result_benchmark

    print_sort_result_benchmark(10, 1, 100, quick_sort)

if __name__ == '__main__':
    main()
