import time
import random

def print_sort_result_benchmark(number_of_elements, arr_start, arr_end, fn):
    arr = [random.randint(arr_start, arr_end) for i in range(number_of_elements)]
    # arr = []
    # while True:
    #     num = random.randint(arr_start, arr_end)
    #     while num not in arr and len(arr) < number_of_elements:
    #         arr.append(num)
    #         num = random.randint(arr_start, arr_end)
    #     break
    
    start_time = time.time()
    sorted_arr = fn(arr)
    end_time = time.time()

    check_if_equals = check_arr_content_equals(arr, sorted_arr)

    print('---------- results ----------')
    print('before')
    print(arr)

    print('after')
    print(sorted_arr)
    print(f'both arrays are equal: {check_if_equals}')
    print('---------- results ----------')

    print('---------- time ----------')

    print('time elapsed: ')
    print(f'--- {end_time - start_time} seconds ---')

    print('---------- time ----------')

def check_arr_content_equals(before, after):
    for _, v in enumerate(after):
        if not v in before:
            return False
    return True
