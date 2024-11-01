t1 = 1*10
t2=3*6
c = 4*10
tempo_viagem = t1 + t2+c
h = 6
m = 52
mf = 52 + tempo_viagem
hf = mf//60
h = h + hf
m = mf%60
print("Chego a casa as {:02d}:{:02d}" .format(h,m))

