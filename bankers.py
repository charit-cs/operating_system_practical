n, m = 5, 3
available = list(map(int, input("Enter available resources: ").split()))
print("Enter Maximum matrix (5 x 3):")
maximum = [list(map(int, input().split())) for i in range(n)]
print("Enter Allocation matrix (5 x 3):")
allocation = [list(map(int, input().split())) for i in range(n)]
need = [[maximum[i][j] - allocation[i][j] for j in range(m)]
        for i in range(n)]

def safe_sequence():
    work = available.copy()
    sequence = []
    while len(sequence) < n:
        found = False
        for i in range(n):
            if i not in sequence and all(need[i][j] <= work[j]
                                         for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                sequence.append(i)
                found = True
        if not found:
            return None
    return sequence

sequence = safe_sequence()
if sequence is None:
    print("System is in an UNSAFE state.")
else:
    print("System is in a SAFE state.")
    print("Safe sequence:", *[f"P{i}" for i in sequence])
    p = int(input("Enter process number (0-4): "))
    request = list(map(int, input("Enter request vector: ").split()))
    if all(0 <= request[j] <= need[p][j] and
           request[j] <= available[j] for j in range(m)):
        for j in range(m):
            available[j] -= request[j]
            allocation[p][j] += request[j]
            need[p][j] -= request[j]
        if safe_sequence() is not None:
            print("Request can be granted safely.")
        else:
            for j in range(m):
                available[j] += request[j]
                allocation[p][j] -= request[j]
                need[p][j] += request[j]
            print("Unsafe request. Process must wait.")
    else:
        print("Request exceeds need or available resources.")