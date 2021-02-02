def ppp():
    age = int(input())
    if age < 0:
        print('Wrong input')
    elif age < 18:
        print('CocaCola')
    else:
        print("Beer")


