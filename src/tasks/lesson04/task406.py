def main2(n,m):
    n1 = int(n)
    m2 = int(m)
    sum_cubes = 0
    for i in range(n1, m2 + 1):
        sum_cubes += i ** 3
    answer = sum_cubes
    return answer



def main():
    n = input("Введите первое число ")
    m = input("Введите второе число ")

    sum_cubes = main2(n, m)

    return sum_cubes


if __name__ == "__main__":
    print(main())