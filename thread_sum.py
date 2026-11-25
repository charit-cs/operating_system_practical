from threading import Thread, Lock

print_lock = Lock()

n = 1000000
chunk = n // 4
results = [0] * 4
threads = []

def sum_array(i):
    start = i * chunk
    end = n if i == 3 else (i + 1) * chunk
    results[i] = sum(range(start, end))
    with print_lock:
        print(f"Thread {i+1}: sum[{start}..{end}) = {results[i]}")

for i in range(4):
    t = Thread(target=sum_array, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Total sum =", sum(results))