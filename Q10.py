
a = int(input("Enter a number: "))

total_swaps = 0
largest = 0

for a in range(n):
    
    for j in range(1, 6):
        swaps = 0
        if a > largest:
            largest = a
            swaps = swaps + 1
    print("Largest number is :", largest)