class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {val: i for i, val in enumerate(list1)}
        map2 = {val: i for i, val in enumerate(list2)}
        # print(map1)
        min_val = 2147483647
        out = []
        for key in map1:
            if key in map2:
                s = map1[key] + map2[key]
                if s < min_val:
                    min_val = s
                    out = [key]
                elif s == min_val:
                    out.append(key)
        return out
