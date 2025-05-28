def sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap 
        nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [10, 3, 2, 17, 7, 5, 9]
sort(nums)
print(nums)
