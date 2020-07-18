#!/usr/bin/python3

import threading
import time

print("Start of the program")


def takeANap():
    time.sleep(5)
    print("Wake up!")


def sayHi(name):
    time.sleep(5)
    print("Hi %s" % name)


threadObj = threading.Thread(target=takeANap)  # main thread and threadObj runs at the same time
# threadObj = threading.Thread(target=takeANap())  # main thread waits for the threadObj to finish before continuing
threadObj.start()
# threadObj.join()  # or you can do this to wait for the background thread to finish

threadObj = threading.Thread(target=sayHi, args=["John"])  # this is how you pass in arguments to the thread
threadObj.start()


print("End of the program")
