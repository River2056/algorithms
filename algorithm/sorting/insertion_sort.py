def insertion_sort(arr):
    for i in range(len(arr)):
        if arr[i] < arr[0]:
            arr.insert(0, arr.pop(i))
        else:
            for j in range(1, i):
                if arr[i] >= arr[j - 1] and arr[i] <= arr[j]:
                    arr.insert(j, arr.pop(i))
    return arr


def main():
    # import custom print function
    import os, sys
    from pathlib import Path

    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
    from common import print_sort_result_benchmark

    print_sort_result_benchmark(10, 1, 100, insertion_sort)


if __name__ == "__main__":
    main()
