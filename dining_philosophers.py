from threading import Thread, Semaphore, Lock
from time import sleep

print_lock = Lock()

n = 5
forks = [Semaphore(1) for i in range(n)]
room = Semaphore(n - 1)

def philosopher(i):
    left = i
    right = (i + 1) % n
    for cycle in range(2):
        with print_lock:
            print(f"Philosopher {i} is thinking")
        sleep(0.01)
        room.acquire()
        forks[left].acquire()
        forks[right].acquire()
        with print_lock:
            print(f"Philosopher {i} is eating (fork {left} and {right})")
        sleep(0.02)
        with print_lock:
            print(f"Philosopher {i} finished eating")
        forks[right].release()
        forks[left].release()
        room.release()

threads = [Thread(target=philosopher, args=(i,)) for i in range(n)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("All philosophers finished.")