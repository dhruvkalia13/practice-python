def findMedianSortedArrays(nums1: [int], nums2: [int]):
    out = []
    len1 = len(nums1)
    len2 = len(nums2)
    i, j = 0, 0
    if (len1 + len2) % 2 == 0:
        find = int((len1 + len2)/2) + 1
        even = True
    else:
        find = int((len1 + len2)/2) + 1
        even = False
    while i < len1 or j < len2:
        if len(out) == find:
            break
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
    find = find-1
    return out[find] if even is False else (out[find] + out[find-1])/2
out = findMedianSortedArrays([1, 3], [2])
print(out)

