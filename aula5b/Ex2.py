# This function reads words from a file.
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            words = line.strip().split()
            lst.extend(words)
    return lst


def matchesPattern(s, pattern):
    s= s.lower()
    pattern = pattern.lower()
    position=0
    if len(s) != len(pattern):
        return False
    for i in range(len(s)):
        if pattern[i] != '?' and s[i] != pattern[i]:
            return False
    return True


def filterPattern(lst,pattern):
    similar=[]
    for word in lst:
        word.lower()
        result = matchesPattern(word, pattern)

        if result == True:
            similar.append(word)
    return similar






def main():
    print("a)")
    print( matchesPattern("secret", "s?c??t") )  #-> True
    print( matchesPattern("secreta", "s?c??t") ) #-> False
    print( matchesPattern("socket", "s?c??t") )  #-> True
    print( matchesPattern("soccer", "s?c??t") )  #-> False
    print( matchesPattern("SEcrEt", "?ecr?t") )  #-> True
    print( matchesPattern("SEcrET", "?ecr?t") )  #-> True
    print( matchesPattern("SecrEt", "?ECR?T") )  #-> True

    words = load("wordlist.txt")

    print("b)")
    # Solution to "S?C??T"
    lst = filterPattern(words, "s?c??t")
    print(lst)

    assert isinstance(lst, list),  "result lst should be a list"
    assert "secret" in lst,  "result should contain 'secret'"

    # Solution to "?YS???Y"
    lst = filterPattern(words, "?ys???y")
    print(lst)


# Call main function:
if __name__ == "__main__":
    main()

#JMR 2022