def validMountainArray(A: [int]) -> bool:
    if len(A) < 3:
        return False
    i = 0
    while i+1 < len(A) and A[i+1] > A[i]:
        i += 1
    if i == len(A)-1 or i == 0: return False
    j = i
    while j+1 < len(A) and A[j+1] < A[j]:
        j += 1
    if j == len(A)-1: return True
    return False


# print(validMountainArray([1,3,2]))
# print(validMountainArray([0,3,2,1]))
# print(validMountainArray([3,5,5]))
# print(validMountainArray([0,1,2,3,4,5,6,7,8,9]))
# print(validMountainArray([0,1,2,3,4,8,9,10,11,12,11]))
print(validMountainArray([9,8,7,6,5,4,3,2,1,0]))

