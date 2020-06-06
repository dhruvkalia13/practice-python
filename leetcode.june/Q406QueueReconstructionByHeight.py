def reconstructQueue(people: [[int]]) -> [[int]]:
    height_desc_func = lambda p: (-p[0], p[1])
    people.sort(key=height_desc_func)
    # print(people)
    res = []
    for person in people:
        res.insert(person[1], person)
    return res


print(reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
