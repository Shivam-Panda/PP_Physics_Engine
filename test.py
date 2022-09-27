import turtle

wn = turtle.Screen()
wn.setup(800, 800)
wn.bgcolor("white")
wn.title("Window")

t = turtle.Turtle()

t.penup()
t.goto(100, 100)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)

while True:
    wn.update()
    if input():
        break
