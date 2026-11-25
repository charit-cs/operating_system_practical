disk = [0] * 30
print("1. Contiguous Allocation\n2. Linked Allocation")
print("3. Indexed Allocation")
choice = int(input("Enter choice: "))
n = int(input("Enter number of files: "))

for f in range(1, n+1):
    free = [i for i in range(30) if disk[i] == 0]
    if choice == 1:
        start, length = map(int, input(f"File {f} - start, length: ").split())
        blocks = list(range(start, start + length))
        if length <= 0 or not all(b in free for b in blocks):
            print("Allocation failed")
            continue
        print(f"File {f} allocated blocks {start} to {blocks[-1]}")
    elif choice == 2 or choice == 3:
        length = int(input(f"File {f} - number of data blocks: "))
        needed = length + (1 if choice == 3 else 0)
        if length <= 0 or needed > len(free):
            print("Allocation failed")
            continue
        blocks = free[:needed]
        if choice == 2:
            chain = " -> ".join(map(str, blocks))
            print(f"File {f}: {chain} -> NULL")
        else:
            print(f"File {f} - Index block: {blocks[0]}, Data blocks:",
                  *blocks[1:])
    else:
        print("Invalid choice")
        break
    for b in blocks:
        disk[b] = 1