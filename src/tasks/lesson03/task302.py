def main():
    x, y = input("Введи любое целое число :"), input("Введи ещё одно любое целое число :")
    z = int(x)+int(y)
    s = f"{x} плюс {y} равно {z}"
    return s


if __name__ == "__main__":
    print(main())