for x in range(0, 20):
    print('привет %s' % x)
    if x > 9:   # Если счет становится больше 9 (Привет 10 больше Привет 9),
        break   # то цикл прерывается (полная остановка выполнения цикла).
                # Если в условии х < 9, то цикл завершился бы на Привет 0.
