import math
def quadratic_equation (a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x_1 = ( (-b) + math.sqrt(discriminant)) / (2 * a)
        x_2 = ( (-b) - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    elif discriminant == 0:
        x_1 = (-b) / (2 * a)
        x_2 = None
        return x_1, x_2 
    elif discriminant < 0:
        x_1 = None
        x_2 = None
        return x_1, x_2
res = quadratic_equation (5, 7, 9)
print(res)