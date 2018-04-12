import random

lst = []
while len(lst) != 9:
    x = random.randint(1, 9)
    if x not in lst:
        lst.append(x)
print(lst)
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)
