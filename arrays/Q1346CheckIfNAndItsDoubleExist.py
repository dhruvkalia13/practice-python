def checkIfExist(arr: [int]) -> bool:
    for i in arr:
        if (i == 0 and arr.count(i) > 1) or (2 * i in arr and arr.index(2 * i) != arr.index(i)):
            return True
    return False


print(checkIfExist([10, 2, 5, 3]))
