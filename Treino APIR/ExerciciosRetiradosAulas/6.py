

def countdown(n):
    print(n)
    if n!=0:
        return countdown(n-1)



def main():
    n = int(input("N:"))
    countdown(n)
main()