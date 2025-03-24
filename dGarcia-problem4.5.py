#-------------------------------------------------------------------------------
# Name:        Chapter 4
# Purpose:     Section 4.9 Problem 2
#
# Author:      DylanG
#
# Created:     03/23/2025
# Copyright:   (c) DylanG 2025
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import turtle
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)
def main ():
    wn = turtle.Screen()        
    wn.bgcolor("lightgreen")
    wn.title("Squares")
    alex = turtle.Turtle()      
    alex.pensize(3)
    alex.pencolor("#FF69B4")
    space = -10

    for i in range(20, 105, 20):
        draw_square(alex, i)
        alex.penup()
        alex.goto(space, space)
        alex.pendown()
        space = space - 10
    wn.exitonclick()
main()    