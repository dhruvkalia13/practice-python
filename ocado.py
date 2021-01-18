# def solution(A, B):
#     # write your code in Python 3.6
#     count = 0
#     if A == 1:
#         A += 1
#         if b >= 2:
#
#     for i in range(A, B+1, 2):
#         flag = 1
#         j = 2
#         while(j * j <= i):
#             if i % j == 0:
#                 flag = 0
#                 break
#             j += 1
#         if (flag == 1):
#             count += 1
#     return count
#
# print(solution(11,19))
# i = "1"*400000

j = "011100"
num = int(j, 2)
# print(num)
# def solution(S):
#     # write your code in Python 3.6
#     a = int(S, 2)
#     count = 0
#     while a > 0:
#         if a % 2 == 0:
#             a //= 2
#         else:
#             a -= 1
#         count += 1
#     return count
# print(solution(i))
# 28
# 011100
# 001000
# def solution(num):
#     # write your code in Python 3.6
#     pot= 1
#     count = 0
#     while pot <= num:
#         val = pot & num
#         if val != 0:
#             count = count + 2
#         else:
#             count = count + 1
#         pot = pot * 2
#     return count - 1
# print(solution(num))

def solution(num):
    s = f'{num:b}'
    return s.count('1')+len(s)-1
print(solution(num))