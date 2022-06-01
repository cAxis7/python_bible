import threading
import time

##hello world
#def hello():
#    print("Hello World!")
#
#t1 = threading.Thread(target=hello)
#t1.start()

#waiting for Threads
#def function1():
#    for x in range(10):
#        print("ONE", end=', ')
#
#def function2():
#    for x in range(10):
#        print("Two", end=', ')
#
#t1 = threading.Thread(target=function1)
#t2 = threading.Thread(target=function2)
#t1.start()
#t2.start()


#def function():
#    for x in range(5000):
#        print('HELLO WORLD!', end=', ')
#
#t1 = threading.Thread(target=function)
#t1.start()
#t1.join(2)
#print("This is the end!")

#Thread Classes
#class MyThread(threading.Thread):
#    def __init__(self, message):
#        threading.Thread.__init__(self)
#        self.message = message
#    
#    def run(self):
#        for x in range(100):
#            print(self.message)
#
#mt1 = MyThread("This is my thread message!")
#mt1.start()

#Synchronizing Threads
#x = 8192
#lock = threading.Lock()
#
#def halve():
#    global x, lock
#    lock.acquire()
#    while(x > 1):
#        x /= 2
#        print(x)
#        time.sleep(1)
#    print('End!')
#    lock.release()
#
#def double():
#    global x, lock
#    lock.acquire()
#    while(x < 16384):
#        x *= 2
#        print(x)
#        time.sleep(1)
#    print('End!')
#    lock.release()
##this two threads will keep printing indefinitely without the locks
##the number will be halved until it reaches the number one and theen it will be double until
##it will double until it reaches the number 16384
#t1 = threading.Thread(target=halve)
#t2 = threading.Thread(target=double)
#
#t1.start()
#t2.start()

#Semaphores

#semaphore = threading.BoundedSemaphore(value=5)
#
#def access(thread_number):
#    print("{}: Trying access...".format(thread_number))
#    semaphore.acquire()
#    print("{}: Access granted!".format(thread_number))
#    print("{}: Waiting 5 seconds...".format(thread_number))
#    time.sleep(5)
#    semaphore.release()
#    print("{}: Releasing!".format(thread_number))
#
#for thread_number in range(10):
#    t = threading.Thread(target=access, args=(thread_number,))
#    t.start()

#Events

#event = threading.Event()
#
#def function():
#    print("Waiting for event...")
#    event.wait()
#    print("Continuing!")
#
#thread = threading.Thread(target=function)
#thread.start()
#
#x = input("Trigger event?")
#if(x == "yes"):
#    event.set()

#Daemon Threads
path = "C:/Users/Juan/Documents/GitHub/python_bible/intermediate/text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open(path) as file:
            text = file.read()
        time.sleep(3)

def printloop():
    global text
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()