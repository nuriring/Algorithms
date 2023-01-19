import sys
sys.stdin = open('2110.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
x_coord = []
for _ in range(N):
    x_coord.append(int(input()))
x_coord.sort()

# start = x_coord[0]
# start_idx = 0
# end_idx = len(x_coord) - 1
# end = x_coord[-1]
# # print(start,end)
# wifi = 2
#
# ans = [start, end]
# while start <= end:
#     if wifi == M:
#         break
#     mid = (start + end) // 2
#     mid_idx = (start_idx + end_idx) // 2
#     if mid == x_coord[mid_idx]:
#         ans.append(mid)
#         wifi += 1
#     elif mid > x_coord[mid_idx]:
#
#         start = mid + 1
#         start_idx = mid_idx + 1
#     else:
#         # ans.append(x_coord[mid_idx])
#         # wifi += 1
#         end = mid - 1
#         end_idx = mid_idx - 1
# # print(house)
#
#
# ans.sort()
# res = []
# print(ans)
# for i in range(len(ans) - 1, 0, -1):
#     res.append(ans[i] - ans[i - 1])
# # print(res)
# print(min(res))

start = 1
end = x_coord[-1] - x_coord[0] #시작값은 최소 거리, 끝 값은 최대 거리
# 앞 집부터 공유기 설치
# 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있으므로
# 설치거리를 mid +1 로 재조정 #가까운 집간의 간격을 넓히는 것임
# c개를 넘어가지 않는다면 더 좁게 설치해야 다 설치할 수 있다는 의미이므로 mid-1
answer = 0
def binary_search(x_coord, start, end):
    global answer
    while start<=end:
        mid = (start+end)//2
        count = 1
        current = x_coord[0]

        for i in range(1,len(x_coord)):
            if x_coord[i] >= current+mid: #첫번째 집과 다음좌표 사이 거리가 현재위치에 mid를 더한값 보다 크거나 같으면 설치가능
                count += 1
                current = x_coord[i]

        if count>=M:
            start = mid+1 #최소M개 만큼 설치가능해졌을때 answer를 기록해야 가장 가까운 집간의 사이 거리를 알수있음
            answer = mid
        else:
            end = mid-1

binary_search(x_coord,start,end)
print(answer)





