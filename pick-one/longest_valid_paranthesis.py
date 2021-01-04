class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0
        output = [0]
        count = 0
        for i, c in enumerate(s):
            if c is "(":
                open += 1
            if c is ")":
                if open == 0:
                    output.append(count)
                    count = 0
                else:
                    open -= 1
                    count += 2
                    if open == 0:
                        output.append(count)
        if open == 0:
            output.append(count)
        # print(output)
        return max(output)


# print(Solution().longestValidParentheses(")()()(()("))
print(Solution().longestValidParentheses("(()"))
# print(Solution().longestValidParentheses("((()))"))
# print(Solution().longestValidParentheses(")()())"))
# print(Solution().longestValidParentheses("()(()"))
