def ispalindrome(str):
    a=""
    for b in str[::-1]:
        a+=b

    if a==str:
        return True
    else:
        return False

print(ispalindrome("OLO"))
print(ispalindrome("OLA"))
print(ispalindrome("9119"))
        