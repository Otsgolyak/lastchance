def chess_reward (seed, n):
    for cell in range(n):
        total_number_of_corns = 2**cell
        if total_number_of_corns >= 1000000:
            return print('На %d клетке \nбудет лежать %d зёрен ' % (cell+1, total_number_of_corns))
chess_reward(0, 64)