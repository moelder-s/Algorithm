arr = [5, 2, 8, 1, 3, 4, 7, 6]

n=len(arr)

print("Original array:", arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print("After each pass:", arr)

print("Sorted array:", arr)