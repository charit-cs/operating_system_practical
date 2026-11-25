pages = list(map(int, input("Enter reference string: ").split()))
n = int(input("Enter number of frames: "))
if n <= 0:
    raise ValueError("Frames must be positive")

for method in ["FIFO", "LRU", "Optimal"]:
    frames = []
    faults = 0
    for i, page in enumerate(pages):
        if page in frames:
            if method == "LRU":
                frames.remove(page)
                frames.append(page)
            continue
        faults += 1
        if len(frames) == n:
            if method == "Optimal":
                future = pages[i+1:]
                victim = max(frames, key=lambda p:
                             future.index(p) if p in future else float("inf"))
                frames.remove(victim)
            else:
                frames.pop(0)
        frames.append(page)
    print(f"{method} Page Faults = {faults}")