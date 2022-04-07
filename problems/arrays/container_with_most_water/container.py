def container_with_most_water(height):
    max_area = 0
    i, j = 0, len(height) - 1
    while i != j:
        w = j - i
        h = min(height[i], height[j])
        area = w * h
        if area > max_area:
            max_area = area
        
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

def main():
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = container_with_most_water(arr)
    print('result: ', result)
    assert result == 49, f'should be 49, got {result} instead'

if __name__ == '__main__':
    main()
