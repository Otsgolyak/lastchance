import random
lst = []
for i in range(11):
    i = random.randint(-1, 1)
    lst.append(i)
print(lst)
def calc_frequency(lst):
    duplicate = []
    a = 0
    b = 0
    c = 0
    #n = lst[i]
    for i in lst[n]:
         n = lst[i]
        if n == (-1):
            a = a+1
        elif i == 0:
            b = b+1
        elif i == 1:
            c = c+1
            return a, b, c
print(calc_frequency(lst))

