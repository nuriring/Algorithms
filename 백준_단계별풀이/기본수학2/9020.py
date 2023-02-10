import sys
input = sys.stdin.readline

def check_prime(N):
    if N == 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            return False
    return True

T = int(input())
for tc in range(T):
    N = int(input())

    a, b = num // 2, num // 2
    while a>0:
        if check_prime(a) and check_prime(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1



