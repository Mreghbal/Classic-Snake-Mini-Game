# Fisst Step: Importing modules & Inputs & Initial records
## Importing required modules
import turtle, time, random, winsound

## Inputs to set a game parameters
name_of_user =  input('Enter your name please:                                                                           ')
screen_color =  input('Enter the screen color, type it carefully:                                                        ')
screen_width =  input('Enter the width of your game screen by numbers carefully, better to be more than 500              ')
screen_height = input('Enter the height of your game screen by numbers carefully, better to be more than 500             ')
head_color =    input('Enter the snake color, type it carefully:                                                         ')
food_color    = input('Enter the snake food color, type it carefully:                                                    ')
pen_color =     input('Enter the scoreboard color, type it carefully:                                                    ')

## Initial records to game playing
delay = 0.15
score = 0
high_score = 0
segments = []
x_right_limit = (int(screen_width) / 2) * 0.97
x_left_limit = (int(screen_width) / 2) * 0.97 * -1
y_up_limit = (int(screen_height) / 2) * 0.97
y_down_limit = (int(screen_height) / 2) * 0.97 * -1
food_right_random_limit = 0.9 * (int(screen_width)) / 2
food_left_random_limit = -0.9 * (int(screen_width)) / 2
food_up_random_limit = 0.9 * (int(screen_height)) / 2
food_down_random_limit = -0.9 * (int(screen_height)) / 2
scoreboard_heigh_position = 0.9 * (int(screen_height)) / 2

# Second Step: Creating components
## Screen
wn = turtle.Screen()
wn.title(f'Snake Game 🐍 with {name_of_user.upper()}     ***github.com/MrEghbal***')
wn.bgcolor(screen_color.lower())
wn.setup(int(screen_width), int(screen_height))
wn.tracer(0)

## Snake's Head
head = turtle.Turtle()
head.shape("circle")
head.color(head_color)
head.penup()
head.goto(0, 0)
head.direction = "Stop"

## Snake's Food
food = turtle.Turtle()
food.speed(0)
food.shape('triangle')
food.color(food_color)
food.penup()
food.goto(0, 100)

## Scoreboard of screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color(pen_color)
pen.penup()
pen.goto(0, scoreboard_heigh_position)
pen.write("Score : 0 High Score : 0", align = "center", font = ("arial", 15, "normal"))
pen.hideturtle()

# Third Step: Move Functions & Keys
## Functions that move snake in response to keyboard keys
def goup():
	if head.direction != "down":
		head.direction = "up"

def godown():
	if head.direction != "up":
		head.direction = "down"

def goleft():
	if head.direction != "right":
		head.direction = "left"

def goright():
	if head.direction != "left":
		head.direction = "right"

def move():
    ### Move the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    ### Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    ### Keep the snake moving
    if head.direction == 'up':
        head.sety(head.ycor() + 15)

    if head.direction == 'down':
        head.sety(head.ycor() - 15)

    if head.direction == 'left':
        head.setx(head.xcor() - 15)

    if head.direction == 'right':
        head.setx(head.xcor() + 15)

## Keyboard key to play game
wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

# Fourth Step: Main game loop
while True:
	wn.update()

	if head.xcor() > x_right_limit or head.xcor() < x_left_limit or head.ycor() > y_up_limit or head.ycor() < y_down_limit:
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
		time.sleep(1)
		head.goto(0,0)
		head.direction = 'stop'

		for segment in segments:
			segment.hideturtle()

		segments.clear()
		score = 0
		delay = 0.15
		pen.clear()
		pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('arial', 15, 'normal'))
		
	if head.distance(food) < 20:
		x = random.randint(food_left_random_limit, food_right_random_limit)
		y = random.randint(food_down_random_limit, food_up_random_limit)
		food.goto(x, y)

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color(head_color)
		new_segment.penup()

		segments.append(new_segment)
		delay -= 0.001
		score += 10

		if score > high_score:
			high_score = score
		pen.clear()
		pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('arial', 15, 'normal'))
	
	move()

	for segment in segments:
		if segment.distance(head) < 10:
			winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
			time.sleep(1)
			head.goto(0,0)
			head.direction = 'stop'

			for segment in segments:
				segment.hideturtle()

			segments.clear()
			score = 0
			delay = 0.15
			pen.clear()
			pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('arial', 15, 'normal'))

	time.sleep(delay)

wn.mainloop()