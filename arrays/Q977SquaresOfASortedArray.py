def sortedSquares(A: [int]) -> [int]:
    return sorted([a ** 2 for a in A])

print(sortedSquares([-4,-1,0,3,10]))
