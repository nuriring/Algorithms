#N은 정수의 개수
N = int(input())
num_list = list(map(int,input().split()))
v = int(input())
# print(v)
cnt = 0
for i in num_list:
    if i == v:
        cnt +=1
print(cnt)