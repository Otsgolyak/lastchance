# string = int(input("Введите любое трехзначное число: " )) # In case with sring, should be changet to str
# #var = int(string[0]) + int(string[1]) + (int(string[2]))
# #print(var)
# digit = string % 100
# digit_1 = digit // 10
# digit_2 = string // 100
# digit_3 = digit % 10

# print(digit_1 + digit_2 + digit_3)

# ver = int(input('Введите трехзначное число: '))
# def sum_of_digits (digit):
#     digit_sum = str(digit)
#     result = int(digit_sum[0]) + int(digit_sum[1]) + int(digit_sum[2])
#     return result
# print(sum_of_digits(ver)) 


ver = int(input('Введите трехзначное число: '))
def sum_of_digits (digit):
    digit_1 = digit // 100
    digit_2 = (digit // 10) % 10
    digit_3 = digit % 10
    result = digit_1 + digit_2 + digit_3
    return result
print(sum_of_digits(ver))