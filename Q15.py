numbers = [5, 10, 15, 20, 25, 30, 35]

def binary_search(numbers, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search(numbers, target, mid + 1, high)
    else:
        return binary_search(numbers, target, low, mid - 1)

result = binary_search(numbers, 25, 0, len(numbers) - 1)
print(result)