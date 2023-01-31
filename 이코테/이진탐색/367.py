n = 7
arr = [1,1,2,2,2,2,3]
target = 2
cnt = 0
from bisect import bisect_left,bisect_right
def binary_search_first(arr,target,start,end):
    # global cnt
    # while start<=end:
    #     mid = (start+end)//2
    #     if arr[mid]==target:
    #         cnt += 1
    #         # return
    #     elif arr[mid]>target:
    #         end = mid - 1
    #     else:
    #         start = mid +1
    if start>end:
        return None
    mid = (start+end)//2
    #해당 값을 가지는 원소 중 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid==0 or target>arr[mid-1]) and arr[mid]==target:
        return mid
    elif arr[mid] >= target:
        return binary_search_first(arr,target,start,mid-1)
    else:
        return binary_search_first(arr,target,mid+1,end)


def binary_search_last(arr,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    #해당 값을 가지는 원소 중 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid==n-1 or target<arr[mid+1]) and arr[mid]==target:
        return mid
    elif arr[mid] > target:
        return binary_search_last(arr,target,start,mid-1)
    else:
        return binary_search_last(arr,target,mid+1,end)

print(binary_search_first(arr,target,0,n-1))
print(binary_search_last(arr,target,0,n-1))
print(bisect_left(arr,2))
print(bisect_right(arr,2))