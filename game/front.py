import threading
import turtle

from data_reader import getter
from package.main import Square, createTarget

WIDTH = int(getter('WIDTH'))
HEIGHT = int(getter('HEIGHT'))
SLOPE = int(getter('XY_SLOPE'))

X = int(getter('TARGET_X'))
Y = int(getter('TARGET_Y'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Front")
wn.bgcolor('white')

createTarget(X, Y)

s = Square(1, 1, "black", 0, 0)

is_running = True

while is_running:
    shoot = bool(getter('SHOOT'))
    if shoot:
        s.slope_movement(SLOPE)
    wn.update()
