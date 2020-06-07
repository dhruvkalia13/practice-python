def twoCitySchedCost(costs: [[int]]) -> int:
    length, a, b, res, i = len(costs), 0, 0, 0, 1
    diff = [((item[1] - item[0]) ** 2) ** (1 / 2) for item in costs]
    map1 = {v: k for v, k in enumerate(diff, start=0)}
    map = {k: v for k, v in sorted(map1.items(), key=lambda item: item[1], reverse=True)}
    print(map)
    for i, diff in map.items():
        # map[]
        item = costs[i]
        ca = item[0]
        cb = item[1]
        if a >= length / 2 or ca > cb and b < length / 2:
            res = res + cb
            b += 1
        elif b >= length / 2 or cb > ca and a < length / 2:
            res = res + ca
            a += 1
    return res

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))