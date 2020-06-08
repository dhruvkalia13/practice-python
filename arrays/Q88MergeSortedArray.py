import bisect
def merge(nums1: [int], m: int, nums2: [int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m + n - 1
    while i >= 0:
        if (m >= 1 and n >= 1 and nums2[n-1] < nums1[m-1]) or n < 1:
            nums1[i] = nums1[m - 1]
            m -= 1
        else:
            nums1[i] = nums2[n - 1]
            n -= 1
        i -= 1
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))