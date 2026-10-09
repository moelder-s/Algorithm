arr = [5, 2, 8, 1, 3, 4, 7, 6]

n=len(arr)

print("Original array:", arr)

total_swaps = 0
for i in range(n):
    swaps=0
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:

            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps = swaps + 1
    total_swaps = total_swaps + swaps
    print("After each pass:", arr)

print("Sorted array:", arr)
print("Total swaps:", total_swaps)