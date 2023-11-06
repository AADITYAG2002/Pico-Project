import _thread
import time

def counting():
    for i in range(10):
        print("num = {}".format(i))
        time.sleep(1)

THREAD_1 = _thread.start_new_thread(counting, ())
counting()