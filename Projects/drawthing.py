#starting stuff
import turtle
t = turtle.Turtle()
t.pensize(40)
t.penup ()
t.goto(0,0)
colors = ["pink", "red", "blue", "green"]
t.pendown()
t.speed(100)
#first i in range
for i in range (450):
  t.forward(2*(i))
  t.left(i*100)
  t.color( colors[ i % 4 ] )
#2nd i in range
t.teleport(0,0)
t.setheading(90)
colors = ["orange", "yellow", "purple", "black"]
for i in range (1000):
  t.forward(2*(i))
  t.left(i*100)
  t.color( colors[ i % 4 ] )
#exit
turtle.exitonclick()
