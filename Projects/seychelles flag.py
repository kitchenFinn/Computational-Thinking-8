import turtle
t = turtle.Turtle()
t.color("blue")
# setup
t.speed(10)



# stripes

# move to stripe 1
t.goto(-360, -280)

# stripe 1
t.color("blue")
t.begin_fill()
t.left(55)
t.forward(800)
t.left(35)
t.forward(200)
t.left(90)
t.forward(500)
t.end_fill()

# move to stripe 2
t.goto(-360, -280)
t.seth(0)
# stripe 2
t.color("yellow")
t.begin_fill()
t.left(55)
t.forward(800)
t.right(35)
t.forward(200)
t.right(145)
t.forward(800)
t.end_fill()

turtle.exitonclick()
