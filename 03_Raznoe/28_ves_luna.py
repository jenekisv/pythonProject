my_ves = 60      # Сейчас мой вес на земле.
ves_god = 1      # Увеличение веса в год на земле.
ves_luna = 0.165 # Лунный вес 16.5% от веса на земле. 
my_ves_luna = my_ves * ves_luna
coins = my_ves_luna
for schet in range(1, 15):                 # Нумерация
    coins = coins + ves_god * ves_luna     # Вычесление
    print('%s Год = %s' % (schet, coins))  # Печать переменных schet и coins
