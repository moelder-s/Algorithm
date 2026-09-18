numbers = [10,20,30,40,50,60,70,80]

print("Before detection:")
print(numbers)

index = int(input("Enter index to delete:"))
for i in range(index, len(numbers) - 1):
    numbers[i] = numbers[i + 1]
numbers.pop()
print("After deletion:", numbers)