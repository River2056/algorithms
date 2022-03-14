male = 5
female = 3
child = 1 / 3

def main():
    # 三種都要買到, 個至少要有一隻
    count = 0
    for i in range(1, 98):
        for j in range(1, 98):
            for k in range(1, 98):
                if ((male * i) + (female * j) + (child * k)) == 100 and (i + j + k) == 100 :
                    print(f'male: {i}, female: {j}, child: {k}')
                    count += 1

    print(f'一共有: {count} 個組合')

if __name__ == '__main__':
    main()
