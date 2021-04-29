
## BINARY SEARCH
# best case - O(logn)
# worst case - O(logn)
## BINARY SEARCH
def binary_search(nums, element):
    mid = 0
    start = 0
    end = len(nums)
    step = 0

    while start <= end:
        step = step+1
        mid = (start + end) // 2

        if element == nums[mid]:
            return mid

        if element < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# print(binary_search([2,3,1,4,5],1))