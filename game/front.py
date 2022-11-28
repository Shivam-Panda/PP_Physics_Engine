import threading
import turtle

from data_reader import get_data
from package.main import Square, createTarget

WIDTH = int(get_data('WIDTH'))
HEIGHT = int(get_data('HEIGHT'))
SLOPE = int(get_data('XY_SLOPE'))

X = int(get_data('TARGET_X'))
Y = int(get_data('TARGET_Y'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Front")
wn.bgcolor('white')

createTarget(X, Y)

s = Square(1, 1, "black", 0, 0)

is_running = True

while is_running:
    shoot = bool(get_data('SHOOT'))
    if shoot:
        s.slope_movement(SLOPE)
    wn.update()
