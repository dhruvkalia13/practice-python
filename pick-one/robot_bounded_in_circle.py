class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        curr = [x, y]
        # facing = ["right", "top", "left", "bottom"]
        r, t, l, d = True, False, False, False
        j = 0
        while j < 4:
            for i in instructions:
                if i == "G":
                    if r:
                        x += 1
                    elif t:
                        y += 1
                    elif l:
                        x -= 1
                    elif d:
                        y -= 1
                    curr = [x, y]
                elif i == "L":
                    if r:
                        r, t, l, d = False, True, False, False
                    elif t:
                        r, t, l, d = False, False, True, False
                    elif l:
                        r, t, l, d = False, False, False, True
                    elif d:
                        r, t, l, d = True, False, False, False
                elif i == "R":
                    if r:
                        r, t, l, d = False, False, False, True
                    elif t:
                        r, t, l, d = True, False, False, False
                    elif l:
                        r, t, l, d = False, True, False, False
                    elif d:
                        r, t, l, d = False, False, True, False
            j += 1
        # print(curr)
        if curr == [0, 0]:
            return True
        return False
