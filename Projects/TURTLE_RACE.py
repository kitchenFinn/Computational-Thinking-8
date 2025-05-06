# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 = random.randint(-400,-385)
y1 = 300
x2 = -405
y2 = 150
x3 = random.randint(-405,-400)
y3 = 0
x4 = -195
y4 = -150
# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("underwater")
t1 = create_sprite("hoop",x1,y1)
t2 = create_sprite("fox",x2,y2)
t3 = create_sprite("corgi",x3,y3)
t4 = create_sprite("can",x4,y4)


# # Section 4 - Racing
# x4 gets a comeback. x1and x2 are close to each other. x2 is the slowest because it goes by 11 each time
# # TODO - explain here which sprites are faster or slower 
for i in range(54):
	x1 += random.randint(random.randint(0,15),random.randint(15,30))
	x2 += 11
	x3 += random.randint(10,20)
	x4 += ((x1)/2)+10
	t1.goto(x1-5, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.01)


# Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("hoooooop winnnssss!")
elif x2 >= x3 and x2 >=x4:
	print("fox W!")
elif x3 >=x4:
	print("corgi wins!")
else:
	print("COMEBACK!")




turtle.exitonclick()
