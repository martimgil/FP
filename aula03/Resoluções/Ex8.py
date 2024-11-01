a = int(input("a? "))
b= int(input("b? "))
c = int(input("c? "))
d= int(input("d? "))

def intersects(a,b,c,d):
   if b<=c: 
      return False
   elif d<=a:
      return False
   else:
      return True



