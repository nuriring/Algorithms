# 2 4 -10 4 -9
import sys
input = sys.stdin.readline
from bisect import bisect_left
N = int(input())
nums = list(map(int,input().split()))
norepeat_nums = set(nums)

sorted_nums = sorted(norepeat_nums)

for i in nums:
    print(bisect_left(sorted_nums,i),end=' ')
