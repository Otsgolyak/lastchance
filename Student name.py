name_surname = 'Anton Golyak'
surname_name = name_surname.split()
list.reverse(surname_name)
#print('Фамилия студента: ', surname_name[0], '\nИмя студента: ', surname_name[1])
print("Фамилия студента: %s \nИмя студента: %s" % (surname_name[0], surname_name[1]))