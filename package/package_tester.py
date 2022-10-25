import threading
import time

from main import Arrow, Shape, Window

w = Window(300, 300, "Testing", "white")

ball = Shape(1, 5, 'black', 'square', 0, 0)
# img = Arrow(1, 5, 0, 0)

class Stop:
    def __init__(self):
        self.go = True

    def end(self):
        self.go = False

stoper = Stop()

def sleeper_bool():
    time.sleep(5)
    print("Done")
    stoper.end()

t1 = threading.Thread(target=sleeper_bool)
t1.start()

while stoper.go:
    ball.horiz_move(0.1)

t1.join()
if input():
    w.quit()
