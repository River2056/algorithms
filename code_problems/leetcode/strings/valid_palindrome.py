import re
import os, sys
from pathlib import Path

sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent))
from common import print_result


def is_palindrome(s):
    replaced = "".join(re.findall(r"[a-zA-Z0-9]", s)).lower()
    reverse = []
    for i in range(len(replaced) - 1, -1, -1):
        reverse.append(replaced[i])
    reverse = "".join(reverse)
    return replaced == reverse


def main():
    print_result("A man, a plan, a canal: Panama", True, is_palindrome)
    print_result("race a car", False, is_palindrome)
    print_result(" ", True, is_palindrome)
    print_result("ab_a", True, is_palindrome)


if __name__ == "__main__":
    main()
