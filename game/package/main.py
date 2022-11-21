import threading
import turtle


class Window:
    def __init__(self, width, height, title, color):
        self.wn = turtle.Screen()
        self.wn.setup(width, height)
        self.wn.title(title)
        self.wn.bgcolor(color)

    def update(self):
        while True:
            self.wn.update()

class Circle:
    def __init__(self, radius, color, x, y):
        self.t = turtle.Turtle()
        self.radius = radius
        self.t.speed(0)
        self.t.shape("circle")
        self.t.shapesize(stretch_wid=radius, stretch_len=radius)
        self.t.color(color)
        self.t.penup()
        self.x = x
        self.y = y
        self.t.goto(x,y)

    def get_pos(self):
        return (self.t.xcor, self.t.ycor)

    def get_radius(self):
        return self.radius
    
    def slope_movement(self, slope):
        if slope == 'vert':
            self.y += 1
            self.t.sety(self.t.ycor() + 1)
        elif slope == 0:
            self.x += 1
            self.t.setx(self.t.xcor()+1)
        else:
            self.x += slope
            self.y += 1
            self.t.setx(self.t.xcor()+slope)
            self.t.sety(self.t.ycor() + 1)

class Square:
    def __init__(self, width, color, x, y):
        self.t = turtle.Turtle()
        self.width = width
        self.t.speed(0)
        self.t.shape("square")
        self.t.shapesize(stretch_wid=width, stretch_len=width)
        self.t.color(color)
        self.t.penup()
        self.x = x
        self.y = y
        self.t.goto(x, y)

    def get_pos(self):
        return (self.x, self.y)

    def get_size(self):
        return self.width

    def slope_movement(self, slope):
        if slope == 'vert':
            self.y += 1
            self.t.sety(self.t.ycor() + 1)
        elif slope == 0:
            self.x += 1
            self.t.setx(self.t.xcor()+1)
        else:
            self.x += slope
            self.y += 1
            self.t.setx(self.t.xcor()+slope)
            self.t.sety(self.t.ycor() + 1)
            
class Stop:
    def __init__(self):
        self.go = True

    def end(self):
        self.go = False

def createTarget(x,y):
    b5 = Circle(5, "black", x,y)
    b4 = Circle(4, "white", x,y)
    b3 = Circle(3, "black", x,y)
    b2 = Circle(2, "white", x,y)
    b1 = Circle(1, "black", x,y)
    return [b1, b2, b3, b4, b5, (x, y)]

def check_collisions(obj, target):
    target_x, target_y = target[len(target)-1]
    x, y = obj.get_pos()
    if target_x == x and target_y == y:
        return True
    return False
