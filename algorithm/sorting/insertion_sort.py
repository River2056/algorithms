def insertion_sort(array):
    arr = [val for val in array]
    for i in range(len(arr)):
        if arr[i] < arr[0]:

    return arr

def main():
    # import custom print function
    import os, sys
    from pathlib import Path
    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent.parent))
    from common import print_sort_result_benchmark

    print_sort_result_benchmark(10, 1, 100, insertion_sort)

if __name__ == '__main__':
    main()
