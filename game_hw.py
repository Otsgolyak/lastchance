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
        return if_less()
    if user_choice < computer_choice:
        return if_more()    

def game ():
    computer_choice = random.randint(1, 10)

    while True:
         user_choice = input('Сделай свой выбор: ')
         valid_user_choice = user_choice.isnumeric() and 1 <= int(user_choice) <= 10
         if valid_user_choice:
             user_choice = int(user_choice) 
             if computer_choice == user_choice:
                print('|************************************|')
                print('|*********Well Done!*****************|')
                print('|************************************|')
                break
             else: 
                user_winner = who_is_winner(user_choice, computer_choice)


game()