import sys
input = sys.stdin.readline

M,N = map(int,input().split())

for i in range(M,N+1):
    prime = True
    # j = 2
    # while j<i:
    #     if i%j==0:
    #         prime = False
    #     j+=1
    #     if not prime:
    #         break

    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            prime = False
            break
    if prime:
        print(i)