a = int(input("Quantos andares tem (sem R/C)?  "))
m = int(input("Quantos moradores por andar tem? "))
#Progressao aritmetica
t1=0
t=2*m*a*3
a=a+1
#Soma dos n termos de uma PA
st=((t1+t)/2)*a
tt=365*st

#Calculo do tempo

h = tt//3600
m = (tt%3600)/60
s=(tt%3600)%60

h=int(h)
m=int(m)
s=int(s)

print("{:02d}:{:02d}:{:02d}".format(h, m, s))