import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('white')

# Makes Everything Work
screen.tracer(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)

while True:
    screen.update()
    
    y = ball.ycor()
    y += 0.01
    ball.sety(y)
