import socket
from queue import Queue
import threading

target = '10.0.0.5'

q = Queue()

for x in range(5000,63001):
    q.put(x)

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False

def worker():
    while True:
        port = q.get()
        if portscan(port):
            print("Port {} is open!".format(port))

for x in range(30):
    t = threading.Thread(target=worker)
    t.start()
print("Done!")