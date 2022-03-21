def main():
    import os, sys
    from pathlib import Path
    sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent.parent))
    from common import generate_random_int_array

    for i in range(500):
        arr = generate_random_int_array(10, 1, 100)
        assert(len(arr) == 10), 'generated array len not match parameter!'

if __name__ == '__main__':
    main()
