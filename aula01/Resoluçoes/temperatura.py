tc = float(input("Temperatura: "))
tf = 1.8*(float(tc)) + 32 #F = 1.8ºC * 32

print(tc, "ºC = ", tf, "ºF") # 10.0ºC = 50.0ºF
#OU
print("{} ºC = {} ºF" .format(tc, tf))
#OU
print("{:^20.4f} ºC = {:02.2f} ºF" .format(tc, tf))
#usar ^ para centrar ou < ou > para colocar os espaços a esquerda ou a direita