found_coins = 20
magic_coins = 70
stolen_coins = 30
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins # Новый счет = текущий счет + полученная сумма за неделю + украденная сумма за неделю
    print('Неделя %s = %s' % (week, coins))    # Печать переменных week и coins
