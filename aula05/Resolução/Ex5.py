# Defina a função aqui.
def countDigits(b):
    count=0
    for i in b:
        if i.isdigit():
            count+=1
        else:
            continue
    return count

def main():
    b = input()
    print("str:", repr(b))
    print("result:", countDigits(b))


if __name__ == "__main__":
    main()
