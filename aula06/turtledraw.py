# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle
f = open("drawing.txt", "r")

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    for line in f:
        print(line)
        i = line.split()
        print ("I:",i)
        if i[0]==str("UP"):
            t.up()
        elif i[0]==str("DOWN"):
            t.down()
        else:
            t.goto(int(i[0]), int(i[1]))

    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()
    f.close()

