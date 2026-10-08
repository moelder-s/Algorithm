#001
array = [35,12,58,21,46,7]

minimum = array[0]

for i in range(1, len(array)):
    if array[i] < minimum:
        minimum = array[i]

print("Minimum value:", minimum)

#002
arr = [64,25,12,22,11]

n = len(arr)

for i in range(n-1):
    min_index = i

    for j  in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted array (Ascending):", arr)

#003
arrr = [5, 2, 9, 1, 5, 6]


n = len(arr)

for i in range(n - 1):
    max_index = i

    for j in range(i + 1, n):
        if arr[j] > arr[max_index]:
            max_index = j

    arr[i], arr[max_index] = arr[max_index], arr[i]
print("Sorted array (Descending):", arr)

