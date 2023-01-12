import sys
sys.stdin = open('197.txt')
N = int(input())
items = list(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))

items.sort()
print(items)
def binary_search(arr,start,end,target):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 'Yes'
        elif target>mid:
            start = mid + 1
        else:
            end = mid + 1
    return 'no'

for i in target:
    print(binary_search(items,0,N-1,i),end=' ')

