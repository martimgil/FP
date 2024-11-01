##
#   Returns a string of asterisks of the same length as
#   a given string.
#   @param string a string such as "secret"
#   @return a string with each character of str changed to a *, such as
#   "******".
#
def hideCharacters(string) :
    n = len(string)
    secret = n*"*"
    return secret

def main():
    string = str(input("Insira palavra:" ))
    print(hideCharacters(string))
main()