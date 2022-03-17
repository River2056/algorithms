import time
import random

def print_sort_result_benchmark(arr_start, arr_end, fn):
    arr = [random.randint(arr_start, arr_end) for i in range(arr_end)]

    start_time = time.time()
    sorted_arr = fn(arr)
    end_time = time.time()

    print('\n---------- results ----------\n')
    print('before')
    print(arr)
    print()

    print('after')
    print(sorted_arr)
    print('\n---------- results ----------\n')

    print('\n---------- time ----------\n')

    print('time elapsed: ')
    print(f'--- {end_time - start_time} seconds ---')

    print('\n---------- time ----------\n')
