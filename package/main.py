import threading
import turtle


class Window:
    def __init__(self, width, height, title, color):
        self.t = threading.Thread(target=self.update)
        self.wn = turtle.Screen()
        self.wn.setup(width, height)
        self.wn.title(title)
        self.wn.bgcolor(color)

        self.t.start()

    def update(self):
        while True:
            self.wn.update()
    
    def quit(self):
        if self.t.is_alive():
            self.t.join()

class Shape:
    def __init__(self, width, length, color, shape, x, y):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape(shape)
        self.t.shapesize(stretch_wid=width, stretch_len=length)
        self.t.color(color)
        self.t.penup()
        self.t.goto(x, y)
    
    def horiz_move(self, interval):
        x = self.t.xcor()
        x += interval
        self.t.setx(x)

    def vertical_move(self, interval):
        y = self.t.ycor()
        y += interval
        self.t.sety(y)

class Stop:
    def __init__(self):
        self.go = True

    def end(self):
        self.go = False
