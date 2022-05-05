def main():
    male = 5
    female = 3
    child = 1 / 3
    count = 0
    for i in range(1, 98):
        for j in range(1, 98):
            child_num = 100 - i - j
            if ((male * i) + (female * j) + (child * child_num)) == 100 and (
                i + j + child_num
            ) == 100:
                print(f"male: {i}, female: {j}, child: {child_num}")
                count += 1
    print(f"一共有{count}個組合")


if __name__ == "__main__":
    main()
