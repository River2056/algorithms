def strip_comments(string, markers):
    """
        Complete the solution so that it strips all text that 
        follows any of a set of comment markers passed in. 
        Any whitespace at the end of the line should also be stripped out.
    """
    arr = string.split('\n')
    for i in range(len(arr)):
        for m in markers:
            if m in arr[i]:
                arr[i] = arr[i][:arr[i].index(m)].strip()
    return '\n'.join(arr)

def main():
    result = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
    print(result)
    assert result == 'apples, pears\ngrapes\nbananas', f'incorrect answer {result}'

    result = strip_comments('a #b\nc\nd $e f g', ['#', '$'])
    print(result)
    assert result == 'a\nc\nd', f'incorrect answer {result}'

if __name__ == '__main__':
    main()
