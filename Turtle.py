import turtle
import random
import time

WIDTH, HEIGHT = 500,500
COLORS = ['blue','green','red','yellow','orange','pink','black','cyan','brown','purple']


def get_numbers_of_racers():
	racers = 0
	while True:
		racers = input("enter the number fo turtles between 2 and 10: ")
		if racers.isdigit():  #checking if the entered valus is digit
			racers = int(racers)
		else:
			print("enter the valid foramt for racers. Try again")
			continue
		if 2 <= racers <= 10 :  #checking the range of turtles
			return racers
		else:
			print("enter the valid racers")
def init_turtle():
	screen = turtle.Screen()      # screen set up for turtle
	screen.setup(WIDTH,HEIGHT)
	screen.title("Turtle Racing")

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors)+1 )
	for i , color in enumerate(colors):  #looping throw turtles
		racer = turtle.Turtle()
		racer.shape("turtle")
		racer.color(color)
		racer.left(90) #to make turtle point upwards
		racer.penup()# not to draw line
		racer.setpos(-WIDTH // 2 + (i+1) * spacingx,-HEIGHT // 2 + 20)  #setting turtles starting position
		racer.pendown()
		turtles.append(racer)

	return turtles

def race(colors):
	turtles = create_turtles(colors)
	while True:
		for j in turtles:
			distance = random.randint(1,20)
			j.forward(distance)

			x , y = j.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(j)]

racers = get_numbers_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"the winner turtle is the turtle with color {winner}")
time.sleep(5)


