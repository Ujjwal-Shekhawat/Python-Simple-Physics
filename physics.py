#More comments will be added later
import turtle
import random

#All functions are defined here
#Physics for .circle
def simy():
    for ball in balls:
        ball.dy += gravity
        ball.sety(ball.ycor() + ball.dy)
        if ball.ycor() < -300:
            ball.dy *= -1

def simx():
    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        if ball.xcor() > 500:
            ball.dx *= -1

        if ball.xcor() < -500:
            ball.dx *= -1

def intercollision():
    for ball in balls:
        ball.pendown()
    for i in range(len(balls)):
        if (balls[i].xcor() == 1):
            balls[i].dx *= -1
            balls[i+1].dx *= -1
#All types of lists exists here
balls = []
colors = ["blue", "green", "red", "yellow", "grey", "white", "aqua", "magenta", "silver"]

wallpaperGenerator = int(input("Would you like to generate a wallpaper out of this 1 or 0 : "))
while True:
    try:
        ballCount = int(input("How many objects do you want : "))
        parse = True
    except:
        print("Enter an numerical value")
        parse = False
    finally:
        if parse == True:
            break

if ballCount <= 0:
    ballCount *= -1
    if ballCount == 0:
        ballCount == 50

while True:
        try:
            simChoice = int(input("Which dimentions to simulate (0D, 1D, 2D)Press 0 or 1 or 2: "))
            parse = True
        except:
            print("Value is not correct enter correct value")
            parse = False
        if parse == True:
            if simChoice != 0 and simChoice != 1 and simChoice != 2:
                print("Enter values 0 or 1 or 2")
                continue
            else:
                break

while True:
        try:
            ballSize = float(input("Enter the ball size (1 is quite big so it is recommended to use valuse between 0 and 1): "))
            parse = True
        except:
            print("Enter an numerical value")
            parse = False
        if parse == True:
            break
            
calculations = 1000/ballCount

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Physics Simulator")
wn.setup(width = 1024, height = 610)
wn.tracer(0)

#All turtle graphics are made here
for i in range(int((500 * 2)/ calculations)):
        balls.append(turtle.Turtle())

#Some variables that will be used in the simulation
x = -500
ballspacing = calculations

for ball in balls:
    y = random.randint(100, 400)
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.penup()
    ball.pensize(1)
    ball.speed(0)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-7, 7)
    ball.turtlesize(ballSize)
    x += ballspacing
        
gravity = -0.1
    
while True:
    wn.update()
    if simChoice == 0:
        print("Simulating in 0D")
    if simChoice == 1:
        print("1D simulation is under devlopement setting the state to 2D simulation")
        simChoice = 2
    if simChoice == 2:
        simy()
        simx()
    if wallpaperGenerator == 1:
        intercollision()
wn.mainloop()
