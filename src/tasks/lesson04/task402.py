def main():
    a = 0
    while 1:
        i = input("number: ")
        if i == "stop":
            break

        if not i.isnumeric():
            print("wrong input")
            continue
        else:
            n = int(i)
            a += n
    return a

if __name__ == "__main__":
    print(main())