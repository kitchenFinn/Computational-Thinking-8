# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Define movement
def move_up():
	s1.setheading(90)
window.onkeypress(move_up, "Up")
def move_up():
	s1.setheading(270)
window.onkeypress(move_up, "Down")
def move_left():
	s1.setheading(180)
window.onkeypress(move_left, "Left")
def move_right():
	s1.setheading(0)
window.onkeypress(move_right, "Right")

# Section 2: Setup
# TODO - create your player character
s1 = create_sprite ("Loco", 0,0)
# TODO - set your background
# TODO - set the starting value for your variable

set_background("Background")

# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control

obstacles = [
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
	create_sprite("cow", random.randint (-200,200), random.randint (-200,200)),
]
# Section 4: Game Loop
window.listen()
timer = 0
s1.goto(0,0)
while True:
	time.sleep(0.01)
	timer += 1  
	# set ("time") == timer 
    
 	# TODO - code for automatic actions

	s1.forward(1)
	if s1.xcor() >= (250):
		print("You lose")
		time.sleep(5)	
		break
	if s1.ycor() >= (200):
		print("You lose")
		time.sleep(5)
		break
	if s1.xcor() <= (-250):
		print("You lose")
		time.sleep(5)
		break
	if s1.ycor() <= (-200):
		print("You lose")
		time.sleep(5)
		break

	# if get_distance
	for s2 in obstacles:
		s2. setheading (random.randint (0, 360))
		if get_distance(s1,s2) < 30:
			s2.hideturtle()
			obstacles.remove(s2)
		s2.forward(2)
		if s2.xcor() >= (250):
			s2.hideturtle()
			obstacles.remove(s2)
		if s2.ycor() >= (200):
			s2.hideturtle()
			obstacles.remove(s2)
		if s2.xcor() <= (-250):
			s2.hideturtle()
			obstacles.remove(s2)
		if s2.ycor() <= (-200):
			s2.hideturtle()
			obstacles.remove(s2)
			
	if len(obstacles) == 0:
		s1.write (f"time is {timer}")
		print(f"You win. Points is {timer}. Lower points are better.")
		time.sleep(5)
		break

	window.update()
