def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Неделя %s, банок: %s' % (week, total_cans))
# Вызывать данную функцию надо = spaceship_building(13), 13 за место cans.
