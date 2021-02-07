def list_processor(lst):
  lst1 = lst.split(",")
  lst2 = []
  for i in lst1:
    try:
      lst2.append(int(i))
    except ValueError:
      continue
  return lst2

def inputs():
  lst = input("Список чисел ")
  lst1 = list_processor(lst)
  more = int(input("Сумма чисел, которые больше "))
  return lst1, more

# lst1 = [1,12,3,4,45]
# more = 10

def main(lst, more_than):
  n = 0
  for i in lst:
    if i > more_than:
      n += i
  return n

if __name__ == "__main__":
  print(main(*inputs()))