import os
import random

from data_reader import *


def init_file():
    set_data('width', 500)
    set_data('height', 500)
    set_data('TARGET_Y', random.randint(-250, 250))
    set_data('TARGET_X', random.randint(-250, 0))
    set_data('VELOCITY', 0)
    set_data('XY_SLOPE', 0)
    set_data('SHOOT', False)
    set_data('VELOCITY', 0)

def side():
    os.system("start /B start cmd.exe @cmd /k python PE/game/side.py")

def camera():
    os.system("start /B start cmd.exe @cmd /k python PE/game/camera.py")

# init_file
camera()
side()