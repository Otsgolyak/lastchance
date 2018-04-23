def chess_reward ():
    ceed = 0
    n = 64
    sum_of_corns = 0
    for cell in range(n):
        total_number_of_corns = 2**(cell-1)
        sum_of_corns += total_number_of_corns
        if total_number_of_corns >= 1000000:
             return cell - 1, total_number_of_corns - 1 
print(chess_reward())

#print('На %d клетке \nбудет лежать %d зёрен ' % (cell+1, total_number_of_corns))