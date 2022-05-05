def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] >= arr[j]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return arr


def main():
    # import custom print function
    import os, sys
    from pathlib import Path

    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
    from common import print_sort_result_benchmark

    # print results
    print_sort_result_benchmark(10, 1, 100, bubble_sort)


if __name__ == "__main__":
    main()
