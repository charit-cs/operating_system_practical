blocks = list(map(int, input("Enter sizes of blocks: ").split()))
processes = list(map(int, input("Enter sizes of processes: ").split()))

for method in ["First Fit", "Best Fit", "Worst Fit"]:
    free = blocks.copy()
    print("\n---", method, "---")
    print("Process No.  Process Size  Block No.")
    for i, size in enumerate(processes):
        choices = [j for j in range(len(free)) if free[j] >= size]
        if not choices:
            block = "Not Allocated"
        else:
            if method == "First Fit":
                j = choices[0]
            elif method == "Best Fit":
                j = min(choices, key=lambda j: free[j])
            else:
                j = max(choices, key=lambda j: free[j])
            free[j] -= size
            block = f"B{j+1}"
        print(f"P{i+1:<12}{size:<14}{block}")