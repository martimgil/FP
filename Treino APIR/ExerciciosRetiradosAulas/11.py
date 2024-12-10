def ispalindrome(s):
    s1=""
    for l in s[::-1]:
        s1+=l

    if s1==s:
        return True
    else:
        return False
        
        
