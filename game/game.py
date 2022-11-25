import os
import random

from data_reader import *


def init_file():
    set_data('width', 500)
    set_data('height', 500)
    # Set Target x, y, z
    set_data('TARGET_X', random.randint(100, 500))
    set_data('TARGET_Y', random.randint(100, 500))
    set_data('TARGET_Z', random.randint(100, 500))
    set_data('XY_SLOPE', 0)
    set_data('YZ_SLOPE', 0)

def front():
    os.system("start /B start cmd.exe @cmd /k python game/front.py")

def side():
    os.system("start /B start cmd.exe @cmd /k python game/side.py")

def camera():
    os.system("start /B start cmd.exe @cmd /k python game/camera.py")

init_file()
camera()
front()
side()