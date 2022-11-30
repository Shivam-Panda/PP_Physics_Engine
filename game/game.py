import os
import random

from data_reader import *


def init_file():
    clear_data()
    set_data('width', 500)
    set_data('height', 500)
    # Set Target x, y, z
    set_data('TARGET_X', random.randint(-250, 250))
    set_data('TARGET_Y', random.randint(-250, 250))
    set_data('TARGET_Z', random.randint(-250, -250))
    # Sample Target Coordinating
    # set_data('TARGET_X', 0)
    # set_data('TARGET_Y', 0)
    # set_data('TARGET_Z', 0)
    set_data('XY_SLOPE', 0)
    set_data('YZ_SLOPE', 0)
    set_data('SHOOT', False)

def front():
    os.system("start /B start cmd.exe @cmd /k python PE/game/front.py")

def side():
    os.system("start /B start cmd.exe @cmd /k python PE/game/side.py")

def camera():
    os.system("start /B start cmd.exe @cmd /k python PE/game/camera.py")

init_file()
# camera()
front()
side()