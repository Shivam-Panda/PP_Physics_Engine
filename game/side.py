import threading
import time
import turtle

from data_reader import get_data
from package.main import Square

WIDTH = int(get_data('width'))
HEIGHT = int(get_data('height'))

X = int(get_data('TARGET_X'))
Y = int(get_data('TARGET_Y'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Side")
wn.bgcolor('white')

global x, y, xy_angle, velocity

x = 200
y = -190

target = Square(5, 1, "red", X, Y)
s = Square(4, 1, "orange", x, y)
aimer = Square(1, 3, "brown", x-20, y)

is_running = True

aimer.turn(-45)

while is_running:
    if bool(get_data('SHOOT')):
        pass
    wn.update()
