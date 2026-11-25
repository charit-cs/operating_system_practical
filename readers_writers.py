from threading import Thread, Semaphore, Lock
from time import sleep

print_lock = Lock()

mutex = Semaphore(1)
wrt = Semaphore(1)
read_count = 0
shared_data = 0

def reader(i):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:
        wrt.acquire()
    mutex.release()

    with print_lock:
        print(f"Reader {i}: read shared_data = {shared_data}")
    sleep(0.02)

    mutex.acquire()
    read_count -= 1
    if read_count == 0:
        wrt.release()
    mutex.release()

def writer(i):
    global shared_data
    wrt.acquire()
    shared_data += 1
    with print_lock:
        print(f"Writer {i}: wrote shared_data = {shared_data}")
    sleep(0.03)
    wrt.release()

threads = [Thread(target=writer, args=(1,))]
for i in range(1, 6):
    threads.append(Thread(target=reader, args=(i,)))
threads.append(Thread(target=writer, args=(2,)))

for t in threads:
    t.start()
for t in threads:
    t.join()