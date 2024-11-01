def main() :
    userInput = input("Enter a string: ")
    spaces = 0
    for char in userInput :
        if char == " " :
            spaces = spaces + 1
    print(spaces)
main()