n = int(input("Enter array size: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

target = int(input("Enter number to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Number found at index:", mid)
        found = True
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Number not Found")