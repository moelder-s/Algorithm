arr = [25, 17, 31, 13, 2, 45, 8]

n = len(arr)

total_comparisons = 0
total_swaps = 0
for i in range(n):
    comparisons = 0
    swaps = 0
    for j in range(0, n-i-1):
        comparisons = comparisons + 1
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps = swaps + 1
    total_comparisons = total_comparisons + comparisons
    total_swaps = total_swaps + swaps
    print("After each pass:", arr)

print("Sorted array (Ascending):", arr)
print("Total comparisons:", total_comparisons)
print("Total swaps:", total_swaps)
