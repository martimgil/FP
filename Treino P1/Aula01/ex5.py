segundos = int(input("Segundos? "))

h = segundos//3600
m = (segundos%3600)//60
s=(segundos%3600)%60
print("{:02d}:{:02d}:{:02d}".format(h,m,s))
