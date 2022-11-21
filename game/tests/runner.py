import threading


def run():
    exec(open('./game/tests/exec.py').read())

def other():
    while True:
        print("noice")

t1 = threading.Thread(target=run) 
t2 = threading.Thread(target=other)
t2.start()
t1.start()