#Create the array
arr = [35,18,62,9,47,25]
#Build a function to find minimum
def find_min_index(arr):
    min_index = 0

    for i in range(1,len(arr)):
        if arr[i]< arr[min_index]:
            min_index = i
    return min_index
print("The index of minimum:",find_min_index(arr))
