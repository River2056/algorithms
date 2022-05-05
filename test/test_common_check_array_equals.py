def main():
    import os, sys
    from pathlib import Path

    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent))
    from common import check_arr_content_equals

    before = [1, 2, 3, 4, 5]
    after = [2, 3, 4, 5, 6, 7]
    check = check_arr_content_equals(before, after)
    assert not check, f"result should be False, Got {check} instead"

    before = [5, 3, 1, 4, 2]
    after = [1, 2, 3, 4, 5]
    check = check_arr_content_equals(before, after)
    assert check, f"result should be True, Got {check} instead"


if __name__ == "__main__":
    main()
