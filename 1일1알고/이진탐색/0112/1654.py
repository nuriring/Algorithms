import sys
sys.stdin = open('1654.txt')

input = sys.stdin.readline

K,N = map(int,input().split())

arr = []
for _ in range(K):
    arr.append(int(input()))

# print(arr)

#가장 긴 랜선 이상으로는 짜를 수 없음
start = 1
end = max(arr)

#적어도 N개 이상은 만들어야함
result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in arr:
        if mid!=0:
            total += (i//mid)
    if total<N:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)