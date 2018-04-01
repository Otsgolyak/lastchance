import random
def if_less ():
    print('|*********************|')
    print('|Заданное число меньше|')
    print('|*********************|')
def if_more ():
    print('|*********************|')
    print('|Заданное число больше|')
    print('|*********************|')    
def who_is_winner (user_choice, computer_choice):
    if user_choice > computer_choice:
        if_less()
    if user_choice < computer_choice:
        if_more()    
def delimiter ():
    print('|*********************|')
    print('|*********************|')
def game ():
    computer_choice = random.randint(1, 10)

    while True:
         delimiter()
         user_choice = input('Сделай свой выбор: ')
         valid_user_choice = user_choice.isnumeric() and 1 <= int(user_choice) <= 10
         if valid_user_choice:
             user_choice = int(user_choice) 
             if computer_choice == user_choice:
                print('|************************************|')
                print('|*********МОЛОДЕЦ!*******************|')
                print('|************************************|')
                break
             else: 
                who_is_winner(user_choice, computer_choice)


game()