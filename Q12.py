arr = [10, 20, 30, 20, 40, 50]

num = int(input("Enter number to remove: "))

found = False

for i in range(len(arr)):
    if arr[i] == num:
        for j in range(i, len(arr) - 1):
            arr[j] = arr[j + 1]

        arr.pop()
        found = True
        break

if found:
    print("Updated array:", arr)
else:
    print("Number not Found")