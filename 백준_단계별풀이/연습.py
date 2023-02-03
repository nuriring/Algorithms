import sys
input = sys.stdin.readline

M,N = map(int,input().split())

for i in range(M,N+1):
    if i==1:
        prime = False
        continue
    prime = True
    j = 2
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            prime = False
            break
    if prime:
        print(i)

from itertools import combinations,permutations