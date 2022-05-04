def is_interesting(number, awesome_phrases):
    if (len(str(number).replace('0', '', -1)) == 1 
            or 
        len(set(str(number).split())) == 1     
            or
            check_if_sequencial(number)
            or
        number in awesome_phrases):
        return 2

def check_if_sequencial(number):
    previous = number % 10
    while number >= 10:
        number /= 10
        n = number % 10
        if ((n < previous and n + 1 != previous) or (n > previous and n - 1 != previous)):
            return False
    return True

def main():
    result = is_interesting(1234, [1337, 256])
    print('result: ', result)

if __name__ == '__main__':
    main()
