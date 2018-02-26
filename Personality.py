#########################################################################################
Name_date = 'Leo Tolstoy*1828-08-28*1910-11-20'
### Выводим из строки str
Separation = Name_date.split('*')
Name = Separation[0]
### Разбиваем даты рождения и смерти
Date1 = Separation[1]
Date_of_birth = Date1.split('-')
Date2 = Separation[2]
Date_of_death = Date2.split('-')
print(Name, 'умер в возрасте:', int(Date_of_death[0]) - int(Date_of_birth[0]), 'лет')
#########################################################################################
###  Надеюсь такой вариант считается выполненным)