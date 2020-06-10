def sortArrayByParity(A: [int]) -> [int]:
    start = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            temp = A[start]
            A[start] = A[i]
            A[i] = temp
            start += 1
    return A