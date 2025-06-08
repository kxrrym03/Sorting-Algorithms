def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

nums = [10, 3, 2, 17, 7, 5, 9]
sort(nums)
print(nums)
