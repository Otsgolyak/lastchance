##### не обращайте внимание на комменты)
#month = (input('Введите месяц: '))
#day = (input('Введите день: '))
#year = (input('Введите год: '))
#american_date = (month, day, year)
#print(american_date)
american_date = '05.17.2018'
needed_date = american_date.split('.')
print ("Дата: ", needed_date[1] + '.'+needed_date[0] + '.' + needed_date[2])