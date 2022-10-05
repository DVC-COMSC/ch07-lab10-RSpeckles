# ******************************
# Make your Code
# ******************************
userInput = input("Enter some values: ")
nums = list(userInput.split())
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    smallest = nums[i]
    flag = 0
    for j in range(i, len(nums)):
        if nums[j] < smallest:
            smallest = nums[j]
            smallestIndex = j
            flag = 1
    if flag == 1:
        nums[smallestIndex] = nums[i]
        nums[i] = smallest
    print(nums)