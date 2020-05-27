class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # loop through the input string char by char
        #     another loop from this char
        #         create a substring untill this char is repeated.
        #             map.put(substring, len(substring))
        #             break
        mapdict = {}
        substr = ""
        if len(s) is 1:
            return 1
        for j in range(0, len(s) - 1):
            index = j
            c = s[index]
            cnext = s[index+1]
            substr = c
            if cnext is not c:
                for i in range(index+1, len(s)):
                    if s[i] in substr:
                        # mapdict[substr] = len(substr)
                        break
                    else:
                        substr = substr + s[i]
                        mapdict[substr] = len(substr)
            else:
                mapdict[substr] = len(substr)
        mapdict[substr] = len(substr)
        return max(mapdict.values()) if len(mapdict) > 0 else 0