def compareFiles():
    with open ("1.txt","rb") as f1, open("2.txt", "rb") as f2:
        while True:
            c1 = f1.read(1024)
            c2 = f2.read(1024)

            if c1 != c2:
                return False
            if not c1:
                return True


print(compareFiles())