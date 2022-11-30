import threading
import time
import turtle

from data_reader import get_data
from package.main import Square

WIDTH = int(get_data('width'))
HEIGHT = int(get_data('height'))

X = int(get_data('TARGET_Z'))
Y = int(get_data('TARGET_Y'))
SLOPE = int(get_data('YZ_SLOPE'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Side")
wn.bgcolor('white')

target = Square(5, 1, "red", X, Y)
s = Square(1, 1, "black", 0, 0)

is_running = True

while is_running:
    shoot = bool(get_data("SHOOT"))
    if shoot:
        s.slope_movement(SLOPE)
    wn.update()
