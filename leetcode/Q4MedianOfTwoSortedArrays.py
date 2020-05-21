def findMedianSortedArrays(nums1: [int], nums2: [int]):
    out = []
    len1 = len(nums1)
    len2 = len(nums2)
    i, j = 0, 0
    while i < len1 or j < len2:
        if len1 <= i:
            out.append(nums2[j])
            j = j + 1
            continue
        elif len2 <= j:
            out.append(nums1[i])
            i = i + 1
            continue
        elif nums1[i] > nums2[j]:
            out.append(nums2[j])
            j = j + 1
        elif nums1[i] <= nums2[j]:
            out.append(nums1[i])
            i = i + 1
    mid = out[int(len(out) / 2)]
    mid1 = out[int(len(out) / 2) - 1]
    median = (mid + mid1) / 2
    print(out)
    return mid if (len1+len2)%2 != 0 else median
out = findMedianSortedArrays([1, 3, 9], [2, 4,6])
print(out)

