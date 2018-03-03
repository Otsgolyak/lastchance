string = int(input("Введите любое трехзначное число: " ))
#var = int(string[0]) + int(string[1]) + (int(string[2]))
#print(var)
digit = string%100
digit_1 = digit//10
digit_2 = string//100
digit_3 = digit%10

print(digit_1+digit_2+digit_3)