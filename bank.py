money = int(input('Введите сумму вклада: '))
time = int(input('Укажите срок вклада: '))
percents = int(input('Укажите процентную ставку по вкладу: '))
sum = money * time 
proc = money * percents / 100
print(proc)
i = 1
while i <= time:
    end_sum = (money + proc) + money
    i = i + 1
print(end_sum)