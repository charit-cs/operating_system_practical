from collections import deque

n = int(input("Enter number of processes: "))
at, bt, pr = [], [], []
for i in range(n):
    a, b, p = map(int, input(f"P{i+1} - AT BT Priority: ").split())
    at.append(a)
    bt.append(b)
    pr.append(p)

print("1. FCFS\n2. SJF\n3. Priority\n4. Round Robin")
choice = int(input("Enter choice: "))
ct = [0] * n
time = 0
order = sorted(range(n), key=lambda i: at[i])

if choice == 4:
    q = int(input("Enter time quantum: "))
    if q <= 0:
        raise ValueError("Quantum must be positive")
    rem = bt.copy()
    ready = deque()
    j = 0
    while j < n or ready:
        if not ready and time < at[order[j]]:
            time = at[order[j]]
        while j < n and at[order[j]] <= time:
            ready.append(order[j])
            j += 1
        i = ready.popleft()
        run = min(q, rem[i])
        time += run
        rem[i] -= run
        while j < n and at[order[j]] <= time:
            ready.append(order[j])
            j += 1
        if rem[i] > 0:
            ready.append(i)
        else:
            ct[i] = time
else:
    pending = order.copy()
    while pending:
        ready = [i for i in pending if at[i] <= time]
        if not ready:
            time = at[pending[0]]
            continue
        if choice == 1:
            i = ready[0]
        elif choice == 2:
            i = min(ready, key=lambda i: bt[i])
        elif choice == 3:
            i = min(ready, key=lambda i: pr[i])
        else:
            raise ValueError("Invalid choice")
        time += bt[i]
        ct[i] = time
        pending.remove(i)

print("PID  AT  BT  CT  TAT  WT")
wt, tat = [], []
for i in range(n):
    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])
    print(i+1, at[i], bt[i], ct[i], tat[i], wt[i], sep="    ")
print(f"Average Waiting Time = {sum(wt)/n:.2f}")
print(f"Average Turnaround Time = {sum(tat)/n:.2f}")