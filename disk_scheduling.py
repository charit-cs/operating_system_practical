requests = list(map(int, input("Enter disk requests: ").split()))
head = int(input("Enter initial head position: "))
size = int(input("Enter disk size: "))

def movement(order):
    total = 0
    current = head
    for track in order:
        total += abs(current - track)
        current = track
    return total

# FCFS: follow arrival order
print("FCFS total head movement =", movement(requests))

# SSTF: choose the nearest request
pending = requests.copy()
current = head
order = []
while pending:
    track = min(pending, key=lambda x: abs(current - x))
    order.append(track)
    pending.remove(track)
    current = track
print("SSTF total head movement =", movement(order))

# SCAN and C-SCAN: initially move towards higher tracks
left = sorted(x for x in requests if x < head)
right = sorted(x for x in requests if x >= head)
scan = right + [size - 1] + left[::-1] if left else right
cscan = right + [size - 1, 0] + left if left else right
print("SCAN total head movement =", movement(scan))
print("C-SCAN total head movement =", movement(cscan))