num = int(input("Значение какого элемента ряда Фибоначчи вы хотите узнать? "))
def fib(num):
    if num==1 or num==2:
        return 1
    return fib(num-1) + fib(num-2)
print(fib(num))