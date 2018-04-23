def chess_reward (seed, n):
   
    sum_of_corns = 0
    for cell in range(n):
        total_number_of_corns = 2**cell
        sum_of_corns += total_number_of_corns
        if total_number_of_corns >= 1000000:
             return cell + 1, sum_of_corns 
print(chess_reward(0, 64))

#print('На %d клетке \nбудет лежать %d зёрен ' % (cell+1, total_number_of_corns))