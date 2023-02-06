import sys
sys.stdin = open('12015.txt')

input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
LIS = []
#기준이 되는 최솟값
LIS.append(arr[0])
#범위가 넓을 때 이진탐색 활용

def lower_bound(arr,num):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == num:
            return mid
        elif num>arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return start




for num in arr:
    if num>LIS[-1]:
        LIS.append(num)
    else:
        idx = lower_bound(LIS,num)
        LIS[idx] = num
print(len(LIS))
# print(LIS)



#dp
N = int(input())  # 6
arr = list(map(int, input().split()))
dp = [1] * (N)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            # arr[i] = arr[j]
            #해당자리의 숫자를 해당자리 이전까지의 숫자와 싹다 비교하면서 더 작은 숫자가 있는 수만큼 누적되면서 길이가 담김
            dp[i] = max(dp[j] + 1, dp[i])