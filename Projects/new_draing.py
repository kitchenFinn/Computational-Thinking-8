#starting stuff
import turtle
t = turtle.Turtle()
t.pensize(40)
t.pendown()
t.goto(0,0)
t.setheading(90)
t.speed(100)
colors = ["orange", "yellow", "purple", "black"]
for i in range (10000):
  t.forward(59)
  t.left(100/(i+1)*100)
  t.color( colors[ i % 4 ] )
t.teleport(0,0)
colors = ["blue", "green"]
for i in range (500):
  t.forward(60)
  t.left(i+40)
  t.color( colors[ i % 2 ] )
#exit
turtle.exitonclick()
