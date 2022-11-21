import threading
import turtle

from data_reader import getter
from package.main import Square, createTarget

WIDTH = int(getter('WIDTH'))
HEIGHT = int(getter('HEIGHT'))

X = int(getter('TARGET_Z'))
Y = int(getter('TARGET_Y'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Side")
wn.bgcolor('white')

s = Square(5, 1, "red", X, Y)

is_running = True

while is_running:
    wn.update()
