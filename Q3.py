nums = [1,4,9,16,25,36,49,81]

print(nums)

index = int(input("Enter index to delete: "))

for i in range(index, len(nums) -1):
    nums[i] = nums[i + 1]

nums.pop()
print("After deletion:" , nums)
