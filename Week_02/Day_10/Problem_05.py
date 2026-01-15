# The Timer (Performance)

import time

def timer(func):
    def wrap():
        start = time.time()
        func()
        print(time.time() - start)
    return wrap


@timer
def implement():
    time.sleep(1)

implement()
