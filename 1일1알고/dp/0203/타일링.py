import sys
sys.stdin = open('타일링.txt')
while True:
    try:
        N = int(input())
        if N<2:

            print(1)

        else:
        # print(N)
            dp = [0]*(N+1)
            dp[1] = 1
            dp[2] = 3
            for i in range(3,N+1):
                dp[i] = dp[i-1] + 2*dp[i-2]
            print(dp[N])
    except EOFError:
        break