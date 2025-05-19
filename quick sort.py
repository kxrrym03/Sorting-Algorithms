def sort(nums):
    def quick_sort_helper(start, end):
        if start < end:
            pivot_index = partition(start, end)
            quick_sort_helper(start, pivot_index - 1)
            quick_sort_helper(pivot_index + 1, end)

    def partition(start, end):
        pivot = nums[end]
        i = start - 1

        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

    quick_sort_helper(0, len(nums) - 1)

nums = [10, 3, 2, 17, 7, 5, 9]
sort(nums)
print(nums)
