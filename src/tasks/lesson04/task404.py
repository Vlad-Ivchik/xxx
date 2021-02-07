def performance(number):
    if number.isdigit():
        number = int(number)
        n = 1
        sum_cubes = 0
        while n <= number:
            sum_cubes += n ** 3
            n += 1
        answer = sum_cubes
    else:
        answer = "Не правильный ввод"
    return answer


def main():
    number = input("Введите целое число ")
    sum_cubes = performance(number)
    return sum_cubes


if __name__ == "__main__":
    print(main())