def get_hint_self(secret: str, guess: str) -> str:
    arr = list(secret)
    arr_guess = list(guess)
    a = 0
    b = 0
    for i in range(len(arr_guess) - 1, -1, -1):
        if arr[i] == arr_guess[i]:
            a += 1
            arr.pop(i)
            arr_guess.pop(i)

    for i in range(len(arr_guess) - 1, -1, -1):
        if arr_guess[i] in arr:
            b += 1
            arr.remove(arr_guess[i])
            arr_guess.remove(arr_guess[i])

    return f"{a}A{b}B"


def get_hint(secret: str, guess: str) -> str:
    h = {}
    a = b = 0
    for elem in secret:
        if not elem in h:
            h[elem] = 1
        else:
            h[elem] += 1

    for i, _ in enumerate(guess):
        if guess[i] in h:
            if guess[i] == secret[i]:
                a += 1
                b -= int(h[guess[i]] <= 0)
            else:
                b += int(h[guess[i]] > 0)
            h[guess[i]] -= 1

    return f"{a}A{b}B"


def test_case(test_secret, test_guess):
    res = get_hint(test_secret, test_guess)
    print(res)


def main():
    test_case("1807", "7810")  # 1A3B
    test_case("1123", "0111")  # 1A1B
    test_case("11", "10")  # 1A0B
    test_case("1122", "1222")  # 3A0B


if __name__ == "__main__":
    main()
