hora = 6
minute = 52
t1 = 10
t2 = 6

tempo = 1 * 10 + 3 * 6 + 4 * 10
minute = 52 + tempo
hora += minute // 60
minute = minute % 60

print(hora, minute)
