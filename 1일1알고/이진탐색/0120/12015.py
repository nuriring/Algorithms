import sys
sys.stdin = open('12015.txt')

input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
LIS = []
#기준이 되는 최솟값
LIS.append(arr[0])
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