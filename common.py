import time
import random

def print_result(test_input, expected, fn):
    result = fn(test_input)
    print('result: ', result)
    assert result == expected, f'should be {expected}, got {result} instead'

def print_sort_result_benchmark(number_of_elements, start, end, fn):
    # arr = [random.randint(arr_start, arr_end) for i in range(number_of_elements)]
    arr = generate_random_int_array(number_of_elements, start, end)
    
    print('---------- results ----------')
    print('before')
    print(arr)
    print('len: ', len(arr))

    start_time = time.time()
    sorted_arr = fn(arr)
    end_time = time.time()

    check_if_equals = check_arr_content_equals(arr, sorted_arr)

    print('after')
    print(sorted_arr)
    print('len: ', len(sorted_arr))
    print(f'both arrays are equal: {check_if_equals}')
    print('---------- results ----------')

    print('---------- time ----------')

    print('time elapsed: ')
    print(f'--- {end_time - start_time} seconds ---')

    print('---------- time ----------')

def check_arr_content_equals(before, after):
    compare_ref_1 = {}
    compare_ref_2 = {}
    for _, v in enumerate(before):
        if v not in compare_ref_1:
            compare_ref_1[v] = 1
        else:
            count = compare_ref_1[v]
            count += 1
            compare_ref_1[v] = count

    for _, v in enumerate(after):
        if v not in compare_ref_2:
            compare_ref_2[v] = 1
        else:
            count = compare_ref_2[v]
            count += 1
            compare_ref_2[v] = count
    
    for key in compare_ref_2:
        if key not in compare_ref_1:
            return False
        if compare_ref_1[key] != compare_ref_2[key]:
            return False
    return True

def generate_random_int_array(number_of_elements, start, end):
    arr = []
    while True:
        if len(arr) == number_of_elements: break
        num = random.randint(start, end)
        if num not in arr: 
            arr.append(num)
    return arr
