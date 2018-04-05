import random
lst = []
for i in range(11):
    i = random.randint(-1, 1)
    lst.append(i)
print(lst)
def calc_frequency(lst):
    
    a = 0
    b = 0
    c = 0
   
    for n in lst:
        
        if n == (-1):
            a = a+1
        elif n == 0:
            b = b+1
        elif n == 1:
            c = c+1
  
    if a>b and a>c:
            return a
    if b>a and b>c:
            return b
    if c>a and c>b:
        return c
    else:
        return None
                        
print(calc_frequency(lst))


