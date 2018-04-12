
num = int(input("Значение какого элемента ряда Фибоначчи вы хотите узнать? "))
def fibo(num):
    fib = [0, 1]
    for i in range(2, num +1 ):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)
    return sum(fib)
        
print(fibo(num))