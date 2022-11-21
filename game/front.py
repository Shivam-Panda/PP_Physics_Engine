import threading
import turtle

from data_reader import getter
from package.main import createTarget

WIDTH = int(getter('WIDTH'))
HEIGHT = int(getter('HEIGHT'))

X = int(getter('TARGET_X'))
Y = int(getter('TARGET_Y'))

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Front")
wn.bgcolor('white')

createTarget(X, Y)

is_running = True

while is_running:
    wn.update()
