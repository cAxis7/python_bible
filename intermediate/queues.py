import queue
import threading
import math

#the default queue type is the so-called FIFO queue.
q = queue.Queue()
threads = []
def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(math.factorial(item))
        q.task_done()

for x in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

zahlen = [134, 14, 5, 30, 98, 88, 11, 23]

for item in zahlen:
    q.put(item)
q.join()
for i in range(5):
    q.put(None)

#LIFO QUEUES

#LIFO stands for last in first out

q = queue.LifoQueue()
numbers = [1,2,3,4,5]
for x in numbers:
    q.put(x)

while not q.empty():
    print(q.get())

# Prioritizing queues

q = queue.PriorityQueue()

q.put((8, "Some string"))
q.put((1, 2023))
q.put((90, True))
q.put((2, 10.23))

while not q.empty():
    print(q.get())
