lst1 = [1,12,3,4,45]
more = 10

def main(lst, more_than):
    n = 0
    for i in lst:
        if i > more_than:
            n += i
    return n


print(main(lst=lst1, more_than=more))
