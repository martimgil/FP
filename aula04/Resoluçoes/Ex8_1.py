import turtle
def spiral(start, end, incr):
    wn=turtle.Screen()
    alex=turtle.Turtle()
    alex.up()
    alex.goto(0,0)
    alex.down()
    alex.color("black")
    alex.shape("turtle")
    for i in range(start, end,incr):
        alex.forward(i)
        alex.left(90)
    wn.mainloop()
def main():
    start=int(input("Start? "))
    end=int(input("End? "))
    r=int(input("range? "))
    spiral(start, end, r)
main()
