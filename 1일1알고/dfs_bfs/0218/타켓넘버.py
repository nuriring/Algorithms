cnt = 0

def dfs(depth, ssum,numbers,target,visited):
    global cnt
    if ssum==target and depth==len(numbers):
        cnt += 1
        return
    for i in ['+','-']:
        for j in range(len(numbers)):
            if visited[j] == 0:
                visited[j] = 1
                if i=='+':
                    dfs(depth+1, ssum + numbers[j],numbers,target,visited)
                else:
                    dfs(depth+1, ssum-numbers[j],numbers,target,visited)

visited = [0]*5
dfs(0,0,[1,1,1,1,1],3,visited)
print(cnt)