def sentence_screen_fitting(sentence: list[str], rows: int, cols: int):
    sentence_str = " ".join(sentence) + " "
    sentence_length = len(sentence_str)

    cursor = 0

    for row in range(rows):
        """
        fill in all cols and pretend as if you are filling in using the sentence_str
        check how many words are filled in (used modulus to check where cursor is)
        act according to cursor position:
        1. if it's a space: move to next word
        2. if it's last letter of a word: move to next word(+2)
        3. in middle of a word: move back till meet a  space
        """
        cursor += cols - 1

        if sentence_str[cursor % sentence_length] == " ":
            cursor += 1
        elif sentence_str[(cursor + 1) % sentence_length] == " ":
            cursor += 2
        else:
            while cursor > 0 and sentence_str[(cursor - 1) % sentence_length] != " ":
                cursor -= 1

    return cursor // sentence_length


def test_case(lst, r, c):
    res = sentence_screen_fitting(lst, r, c)
    print(res)


def main():
    test_case(["hello", "world"], 2, 8)  # 1
    test_case(["a", "bcd", "e"], 3, 6)  # 2
    test_case(["i", "had", "apple", "pie"], 4, 5)  # 1

    # line = "abc "
    # print(100 // len(line))
    # print(100 % len(line))


if __name__ == "__main__":
    main()
