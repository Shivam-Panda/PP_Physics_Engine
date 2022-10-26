import threading
import time

from main import Shape, Stop, Window

w = Window(300, 300, "Testing", "white")

ball = Shape(1, 5, 'black', 'square', 0, 0)
square = Shape(5, 1, "green", "square", 0, -200)
# img = Arrow(1, 5, 0, 0)

objects = [ball, square]


stoper_1 = Stop()
stoper_2 = Stop()

stoppers = [stoper_1, stoper_2]
movements = ['hor', (2,1)]

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

def all_false(stoppers):
    for i in stoppers:
        if i.go is True:
            return False
    return True

while True:
    for i in range(len(objects)):
        if stoppers[i].go:
            if movements[i] == 'hor':
                objects[i].horiz_move(1)
            elif movements[i] == 'ver':
                objects[i].horiz_move(1)
            elif type(movements[i]) is not "<class 'str'>":
                objects[i].vertical_move(movements[i][0])
                objects[i].horiz_move(movements[i][1])
    
    if all_false(stoppers):
        break

if input():
    w.quit()
