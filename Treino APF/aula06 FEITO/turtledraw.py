# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    with open("drawing.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line=="UP":
                t.up()
            elif line=="DOWN":
                t.down()
            else:
                line = line.split(" ")
                t.goto(int(line[0]), int(line[1]))
    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

