# import sys
# sys.stdin = open('1300.txt')
# input = sys.stdin.readline
#
# N = int(input())
# K = int(input())
# B = []
#
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         B.append(i*j)
# print(B)
# B.sort()
# print(B[K])

# start = 0
# end = N*N
# answer = 0
# while start<=end:
#     mid = (start+end)//2
#     total = 0
#     for i in range(1,N+1):
#         if mid//i >N:
#             total += N
#         else:
#             total += mid//i
#     if total == K:
#         pass
#         # print("바보야")
#         # break
#     elif total>K:
#         end = mid-1
#     else:
#         start = mid +1
# print(mid)

import sys
sys.stdin = open('1300.txt')
input = sys.stdin.readline

N = int(input())
K = int(input())
# B = []
#
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         B.append(i*j)
# print(B)
# B.sort()
# print(B[K])

start = 0
end = N*N
answer = 0
def binary_search(start,end):
    global answer
    while start<=end:
        mid = (start+end)//2
        total = 0
        for i in range(1,N+1):
            if mid//i >N:
                total += N
            else:
                total += mid//i
        if total >= K: #작은 수가 최소 K개에 도달하면 그때 mid가 해당번째의 수가 됨
            answer = mid
            end = mid-1
        # elif total>K:
        #     end = mid-1
        else:
            start = mid +1

binary_search(start,end)
print(answer)

