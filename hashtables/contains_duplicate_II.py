class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = {}
        for idx, i in enumerate(nums):
            if i in nums_map:
                nums_map[i].append(idx)
            else:
                nums_map[i] = [idx]
        for key, val in nums_map.items():
            if len(val) > 1:
                temp = set()
                for idx in range(1,len(val)):
                    temp.add(val[idx] - val[idx-1])
                if min(temp) <= k:
                    return True
        return False