import turtle


class Window:
    def __init__(self, width, height, title, color):
        self.wn = turtle.Screen()
        self.wn.setup(width, height)
        self.wn.title(title)
        self.wn.bgcolor(color)

class Pen:
    def __init__(self):
        self.pen = turtle.Turtle()
