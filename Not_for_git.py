###########################################################################

#print (float("210" * int("2")))

###########################################################################
###########################################################################

#print ( 10 == 11) ##### - узнаем равно ли 10 11, выдаст  True когда равно и False когда не равно #####

################################################################################################

#print ( 10 != 11) #### - функция не равно. Выдает True когда не равно и False когда равно ######

###################################################################################################

#print ( 5 >= 5 ) ##### - Так же само выводит True или False, так же есть <=

#################################################################################################

#print ( "Test" > "Tesa") ##### - Лексогравическое сравнение. Сравнивает вес строк. Каждая буква имеет свой вес: (а - 1,
                        ######## b - 2) Регистр букв на вес не влияет

######################################################################################################

#pogoda = "Зима"                             ##### - если будет не 'Зима' - ничего не запустится
#if  pogoda == "Зима":                       ##### - if это условие
#    print ("Сиди дома!")

######################################################################################
######################################################################################
#                           #####  Вложенное условие  #####
#pogoda = "Зима"
#time = 'Ночь'
#print('Программа запущена.')
#if  pogoda == "Зима":
#    print ("Сиди дома!")
#    if  time == 'Ночь':
#        print('Спааааать!!!')
#if  pogoda == "Дождь":
#    print ("Мокренькая кисонька")
#print ("End")

#######################################################################################
#######################################################################################
############################ Калькулятор ^_^ ##########################################
#var_1 = int(input('Введите первую переменную: '))
#var_2 = int(input('Введите вторую переменную: '))
#operation = input('Введите условие: ')
#if operation == '+':
#    print('Ответ: ', var_1 + var_2)
#if operation == '-':
#    print('Ответ: ', var_1 - var_2)
#if operation == '*':
#    print('Ответ: ', var_1 * var_2)
#if operation == '/':
#    print('Ответ: ', var_1 / var_2)
#print('Конец')

#######################################################################################
#######################################################################################
#                       #########  Else $ Elif  ######################    video 5        
#######################################################################################

#time = 'ночь'

#if time == 'ночь':
#    print('Ты псих? Сейчас же ночь!')
#elif time == 'утро':
#    print('Ты хоть позавтракал?')
#elif time == 'день':
#    print('Гулять можноб кэп!')
#elif time == 'вечер':
#    print('Гулять можноб кэп!')
#else:
#    print('Error')

#######################################################################################
######################################## video 6#######################################
########             #######  Множественные условия, приоритетность операторов   ######
#######################################################################################

#pogoda = 'дождь'
#time  = 'ночь'
#if pogoda == 'дождь' and ( time == 'ночь' or time == 'вечер' ):   # Можно взять в скобки для лучшей читабельности
#    print('Какую то строку')

########################################################################################
#######             ####  Not  #####################################        ############    

#pogoda = 'дождь'
#if not pogoda == 'снег':
#    print('что-то')

########################################################################################
############################    video 7     ############################################
#######     ##################      Циклы       ##############      ####################
########################################################################################

#i = 1
#while i <= 5:
#    print(i)
#    i += 1

#######################  Бесконечный цикл)))   #########################################

#i = 1
#while 1 == 1:
#    print('WaagH, ' + str(i))
#    i += 1

########################################################################################
###########################  НЕ РАБОТАЕТ!!! ###########################################
#i = 1
#while 1 == 1:
#    print('WaagH, ' + str(i))
#    i = i + 1
#    if i == 1000:
#        break   
#print('WAAAAAAGGGGHHHHHH')

##########################################################################################

#number = 0
#while number <= 100:
#    number += 1
#    if (number % 2) != 0:
#        continue
#    print('Четное число' + str(number))

##########################################################################################
#######     #########       Списки  video 8         ######################################
##########################################################################################
'''
test = [1,3,5,7,9]
if 3 in test:
    print('3')
if 4 not in test:
    print('В списке нет четных чисел')
'''
####################################################################################################
#import math
 
 
#def calc_interception(x1, y1, r1, x2, y2, r2):
 #   cen_dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#    if not cen_dist:
 #       return "Нет" if r1 != r2 else "Да"
#    else:
 #       return "Нет" if cen_dist > r1 + r2 else "Да"
 
#data = []
#while True:
#    line = input()
#    if not line:
#        break
 #   data.append(float(line))
 
#print(calc_interception(*data))

import random

text = 'abracadabra'
text = list(text)
random.shuffle(text)
print(text)