def fibo(n):
    global cnt
    if n==1 or n==2:
        cnt+=1
        return 1
    else:

        return fibo(n-1)+fibo(n-2)

def dp_fibo(n):
    global cnt_dp
    dp = [0]*40
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        cnt_dp+=1
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

cnt = 0
cnt_dp = 0
fibo(5)
dp_fibo(5)
print(cnt,end=" ")
print(cnt_dp)
