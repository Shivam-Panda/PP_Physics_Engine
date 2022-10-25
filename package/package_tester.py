import threading
import time

from main import Shape, Window

w = Window(300, 300, "Testing", "white")

ball = Shape(1, 5, 'black', 'square', 0, 0)
square = Shape(5, 1, "green", "square", 0, -200)
# img = Arrow(1, 5, 0, 0)

class Stop:
    def __init__(self):
        self.go = True

    def end(self):
        self.go = False

stoper_1 = Stop()
stoper_2 = Stop()

def sleeper_bool():
    time.sleep(5)
    print("Done")
    stoper_1.end()

def sleeper_ender():
    time.sleep(10)
    print("Done Job 2")
    stoper_2.end()

t1 = threading.Thread(target=sleeper_bool)
t2 = threading.Thread(target=sleeper_ender)

t1.start()
t2.start()

while True:
    if stoper_1.go:
        ball.horiz_move(0.1)

    if stoper_2.go:
        square.vertical_move(0.1)

    if stoper_2.go is False and stoper_1.go is False:
        break

if input():
    w.quit()
