
# QUICK SORT
# worst case - n square (already sorted)
# best case - nlogn
# QUICK SORT
def quicksort(nums):
    helper_quick_sort(nums, 0, len(nums)-1)

def helper_quick_sort(nums, start, end):
    if start < end:
        pivot = partition(nums, start, end)
        helper_quick_sort(nums, start, pivot - 1)
        helper_quick_sort(nums, pivot + 1, end)

def partition(nums, start, end):
    middle = (start + end) // 2
    # swapping middle with end
    nums[middle], nums[end] = nums[end], nums[middle]
    pivot = nums[end]
    boundary = start
    # Move items less than pivt to the left
    for index in range(start, end):
        if nums[index] < pivot:
            nums[boundary], nums[index] = nums[index], nums[boundary]
            boundary += 1
    # Exchange the pivot item and the boundary item
    nums[boundary], nums[end] = nums[end], nums[boundary]
    return boundary