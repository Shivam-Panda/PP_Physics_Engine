import threading
import time

from main import Circle, Square, Stop, Window, check_collisions, createTarget

w = Window(300, 300, "Testing", "white")

updater=threading.Thread(target=w.update, daemon=True)
updater.start()

square = Square(1, "green", 0, -200)
target = createTarget(0, 0)

stoper_2 = Stop()

def sleeper_ender():
    time.sleep(10)
    print("Done Job 2")
    stoper_2.end()

t2 = threading.Thread(target=sleeper_ender, daemon=True)

t2.start()

while True:
    if (check_collisions(square, target)):
        break

    if stoper_2.go:
        square.slope_movement('vert')
    else:
        break

if input():
    updater.join()