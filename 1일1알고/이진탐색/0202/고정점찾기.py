def binary_search(arr,start,end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==mid:
            return mid
        elif arr[mid]>mid:
            end = mid-1
        else:
            start = mid+1
    return -1

arr = [-15,-4,3,8,9,13,15]

print(binary_search(arr,0,len(arr)))