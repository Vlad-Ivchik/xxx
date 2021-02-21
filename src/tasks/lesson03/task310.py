

def main2():
    x = input("Введи деньги в формате 22.32 ")
    y = x.split(".")
    z = int(y)

    if len(y[0]) == 0:
        print("Ноль рублей")
