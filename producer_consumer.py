from threading import Thread, Semaphore
from time import sleep

size = 5
buffer = [0] * size
empty = Semaphore(size)
full = Semaphore(0)
mutex = Semaphore(1)

def producer():
    for item in range(1, 11):
        empty.acquire()
        mutex.acquire()
        slot = (item - 1) % size
        buffer[slot] = item
        print(f"Producer produced item {item} at slot {slot}")
        mutex.release()
        full.release()
        sleep(0.01)

def consumer():
    for i in range(10):
        full.acquire()
        mutex.acquire()
        slot = i % size
        item = buffer[slot]
        print(f"Consumer consumed item {item} from slot {slot}")
        mutex.release()
        empty.release()
        sleep(0.015)

p = Thread(target=producer)
c = Thread(target=consumer)
p.start()
c.start()
p.join()
c.join()
print("All items produced and consumed.")