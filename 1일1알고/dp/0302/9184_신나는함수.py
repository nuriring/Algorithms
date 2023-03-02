from collections import defaultdict
dp = defaultdict(int)
import sys
input = sys.stdin.readline
def w(a,b,c):
    #종료조건
    if a<=0 or b<=0 or c<=0:
        return 1
    #아직 계산해본적 없다면
    if a>20 or b>20 or c>20:
        dp[(a,b,c)] = w(20,20,20)
        return dp[(a,b,c)]
    #이미 계산한적 있다면 그대로 반환
    if dp[(a,b,c)] != 0:
        return dp[(a,b,c)]
    if a<b and b<c:
        dp[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[(a,b,c)] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[(a,b,c)]
while True:
    a,b,c = map(int,input().split())
    if (a,b,c) == (-1,-1,-1):
        break
    ans = w(a,b,c)

    print(f'w({a}, {b}, {c}) = {ans}')



