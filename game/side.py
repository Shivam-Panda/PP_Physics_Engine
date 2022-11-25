import threading
import turtle

from data_reader import getter
from package.main import Square, createTarget

WIDTH = int(getter('WIDTH'))
HEIGHT = int(getter('HEIGHT'))

X = int(getter('TARGET_Z'))
Y = int(getter('TARGET_Y'))
SLOPE = int(getter('YZ_SLOPE'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Side")
wn.bgcolor('white')

target = Square(5, 1, "red", X, Y)
s = Square(1, 1, "black", 0, 0)

is_running = True

while is_running:
    shoot = bool(getter("SHOOT"))
    if shoot:
        s.slope_movement(SLOPE)
    wn.update()
