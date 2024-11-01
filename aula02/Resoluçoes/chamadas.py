t =int(input("Tempo(seg)): "))
    
p1 = 0.12
p2 = 0.06

if t <= 60:
    print("Preço:", p1)
else: 
    t_resto = t - 60
    t_30 = t_resto//30
    p = p1 + p2 * t_30
    print("Preço: ", p)

