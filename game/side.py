import math
import threading
import time
import turtle

from data_reader import get_data
from package.main import Circle, Square

WIDTH = int(get_data('width'))
HEIGHT = int(get_data('height'))

# X = int(get_data('TARGET_X'))
# Y = int(get_data('TARGET_Y'))

X = -200
Y = 0

wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Side")
wn.bgcolor('white')

global x, y

x = 200
y = 0

xa = 200
ya = 0

target = Circle(4, "red", X, Y)
s = Square(4, 1, "orange", x, y)
aimer = Square(1, 3, "brown", x-20, y)
arrow = Square(1, 1, "black", xa, ya)

is_running = True

global final_slope
final_slope = get_data('XY_SLOPE')

global velocity
velocity = float(get_data('VELOCITY'))

global done
done = False

global shot
shot = False

def check_collisions(x, y, X, Y):
    dist = arrow.t.distance(target.t.pos())
    print(dist)
    if dist < (45):
        return True
    else:
        return False

while is_running:
    if done == False:
        X = get_data('XY_SLOPE')
        if X:
            final_slope = float()
            aimer.turn(float(math.degrees(X)))

        v = get_data('XY_SLOPE')
        if v:
            velocity = float(v)
    if bool(get_data("SHOOT")):
        v = get_data('XY_SLOPE')
        if v:
            velocity = float(v)
        X = get_data('XY_SLOPE')
        if X:
            final_slope = float(X)

        shot = True
        break
    wn.update()

while shot:
    arrow.x_inc(-1)
    xa -= 1
    ya += math.tan(final_slope)
    arrow.y_inc(math.tan(final_slope))
    if check_collisions(xa, ya, get_data('TARGET_X'), get_data('TARGET_Y')):
        break
    wn.update()

print("You Won")
