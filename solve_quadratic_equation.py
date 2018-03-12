import math
def quad (a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = ( (-b) + math.sqrt(D)) / (2 * a)
        x2 = ( (-b) - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x1 = (-b) / (2 * a)
        x2 = None
        return x1, x2 
    elif D < 0:
        x1 = None
        x2 = None
        return x1, x2
res = quad (5, 7, 9)
print(res)