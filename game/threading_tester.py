import threading
import time

from package.main import Window


def worker():
    w = Window(300, 300, "Tester", "black")
    u = threading.Thread(target=w.update, daemon=True)
    u.start()
    time.sleep(3)
    print("Closing")
    u.join()

t1=threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t1.start()
t2.start()
