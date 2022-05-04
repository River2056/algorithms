def reverse(string):
    return string[::-1]

def reverse_str_recursive(word, result = ''):
    if len(word) == 0:
        return result
    result += word[-1:]
    return reverse_str_recursive(word[0:-1], result)

def reverse_str_iterative(word):
    result = ''
    for _ in enumerate(word):
        result += word[-1:]
        word = word[0:-1]
    return result

def main():
    print(reverse('yoyo mastery'))
    print(reverse_str_recursive('yoyo mastery'))
    print(reverse_str_iterative('yoyo mastery'))

if __name__ == '__main__':
    main()
