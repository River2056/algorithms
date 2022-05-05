def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] <= arr[min_index]:
                min_index = j
        t = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = t
    return arr


def main():
    # import custom print function
    import os, sys
    from pathlib import Path

    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
    from common import print_sort_result_benchmark

    print_sort_result_benchmark(10, 1, 100, selection_sort)


if __name__ == "__main__":
    main()
