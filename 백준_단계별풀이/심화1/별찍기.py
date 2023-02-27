#123454321
#135797531
# (2*n-1 - (1~2*n-1까지 2씩 늘어남))//2 +  1~2*n-1까지 2씩 늘어남 (2*n-1 - (1~2*n-1까지 2씩 늘어남))//2
# 4 1 4
# 3 3 3
# 2 5 2
n = int(input())
for i in range(1,2*n,2):
    space = (2*n-1 - i)//2
    print(' '*space + '*'*i)
for i in range(2*n-3,0,-2):
    space = (2 * n - 1 - i) // 2
    print(' '*space + '*'*i)


