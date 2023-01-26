#이동가능한 동선
dx=[-1,1,-1,1,-2,-2,2,2]
dy=[2,2,-2,-2,1,-1,1,-1]

now = input()
y = ord(now[0:1])%97+1
x = int(now[1:])

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1<=nx<=8 and 1<=ny<=8:
        cnt += 1

print(cnt)

