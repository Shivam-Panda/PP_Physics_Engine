import threading
import time
import turtle

from main import Square, Stop, check_collisions, createTarget

wn = turtle.Screen()
wn.setup(500, 500)
wn.title("Demo")
wn.bgcolor("White")

updater=threading.Thread(target=wn.update, daemon=True)
updater.start()

square = Square(1,1, "green", 0, -200)
square = Square(1,5, "brown", 15, -15)
square = Square(6,2, "red", 26, 150)
square = Square(1,3, "blue", -200, 200)
square = Square(2,2, "black", -100, -100)
# target = createTarget(0, 0)

stoper_2 = Stop()

def sleeper_ender():
    time.sleep(1)
    print("Done Job 2")
    stoper_2.end()

t2 = threading.Thread(target=sleeper_ender, daemon=True)

t2.start()

while True:
    # if (check_collisions(square, target)):
    #     break

    if stoper_2.go:
        square.slope_movement('vert')
    else:
        break

if input():
    updater.join()