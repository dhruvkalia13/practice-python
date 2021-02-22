class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map, nums2_map = {}, {}
        for idx, i in enumerate(nums1):
            if i in nums1_map:
                nums1_map[i] += 1
            else:
                nums1_map[i] = 1
        for idx, i in enumerate(nums2):
            if i in nums2_map:
                nums2_map[i] += 1
            else:
                nums2_map[i] = 1
        out = []
        for i in nums1_map:
            if i in nums2_map:
                out.extend([i] * (min(nums1_map[i], nums2_map[i])))
        return out

