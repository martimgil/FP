def contida(principal, sub):
    for item in sub:
        encontrado = False

        for i in range(len(principal)):
            if principal[i] == item:
                encontrado = True
                break
        
        if not encontrado:
            return False
    return True

def main():
    assert(contida([1, 2, 3, 4, 5], [2, 3]) == True)
    assert(contida([2, 4, 6, 8], [10, 12]) == False)
    assert(contida([0, 1, 2], [1]) == True)

    print("All tests passed!")

if __name__ == "__main__":
    main()