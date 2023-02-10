import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N==0:
        break
    # print(N)
    cnt = 0
    for i in range(N+1, 2*N+1):
        prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                prime=False
                break
        if prime:
            cnt += 1
    print(cnt)

