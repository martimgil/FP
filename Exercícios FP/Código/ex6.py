def capicua(num):
    original = num
    invertido = 0
    
    if num < 0:
        return False

    while num > 0:
        digit = num % 10
        invertido = invertido * 10 + digit
        num = num // 10

    return original == invertido

def main():
    assert(capicua(19891) == True)
    assert(capicua(251) == False)
    assert(capicua(101) == True)
    assert(capicua(2) == True)
    assert(capicua(-11) == False)
    print("All tests passed!")

if __name__ == "__main__":
    main()