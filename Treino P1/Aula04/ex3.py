print("n", "Un")
Un = 100
n = 0# Un = each term of the sequence. Initially = U0
while Un>0:
    print(n, Un)
    Un = 1.01*Un - 1.01
    n +=1 #
print("Foram obtidos", n)