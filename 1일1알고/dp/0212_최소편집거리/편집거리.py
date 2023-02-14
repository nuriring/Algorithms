import sys
sys.stdin = open('편집거리.txt')

#최소 편집 거리를 위한 다이나믹 프로그래밍
def edit_dist(str1, str2):
    a = len(str1)
    b = len(str2)

    dp = [[0]*(a+1) for _ in range(b+1)]
    for j in range(1,a+1):
        dp[0][j] = j
    for i in range(1,b+1):
        dp[i][0] = i
    print(dp)
    for j in range(1,a+1):
        for i in range(1,b+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) +1
    print(dp[b-1][a-1])



str1 = input()
str2 = input()
edit_dist(str1,str2)




