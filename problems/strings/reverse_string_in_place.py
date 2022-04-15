def reverse_string_self(s):
    last = len(s) - 2
    for i in range(len(s)):
        s.append(s.pop(last))
        last -= 1

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def main():
    arr = ['h', 'e', 'l', 'l', 'o']
    reverse_string(arr)
    assert arr == ['o', 'l', 'l', 'e', 'h'], f'wrong answer: {arr}'

    arr = ['H', 'a', 'n', 'n', 'a', 'h']
    reverse_string(arr)
    assert arr == ['h', 'a', 'n', 'n', 'a', 'H'], f'wrong answer: {arr}'

    arr = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
    reverse_string(arr)
    assert arr == ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"], f'wrong answer: {arr}'

if __name__ == '__main__':
    main()
