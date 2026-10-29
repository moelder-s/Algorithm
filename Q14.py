numbers = [10, 20, 30, 40, 50, 60, 70]

def binary_search(target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

result = binary_search(40)

if result != -1:
    print("Number 40 found at index:", result)
else:
    print("Number not found")

result = binary_search(25)

if result != -1:
    print("Number 25 found at index:", result)
else:
    print("Number 25 not found")