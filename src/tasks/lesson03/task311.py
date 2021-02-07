def main():
    x = input("Введите свой e-mail: ")

    y = x.split("@")

    if y[1] == "gmail.com":
        print(x)
    else:
        print("DOMAIN NAME is not supported")

if __name__ == "__main__":
    main()