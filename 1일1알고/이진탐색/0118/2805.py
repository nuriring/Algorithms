import sys
sys.stdin = open('2805.txt')

input = sys.stdin.readline

N,M = map(int,input().split())
#N은 나무의 수 #M은 나무의 길이
#M을 가져가기 위해 절단기에 설정할 수 있는 최댓값

trees = list(map(int,input().split()))
#일단 절단기는 max_height 는 못 넘음

max_height = max(trees)
start = 0
end = max_height

answer = []
while start<=end:
    mid = (start+end)//2
    total = 0
    for tree in trees:
        if tree>mid:
            total += (tree-mid) #베인나무
    if total >= M: #적어도 M 이상이면 최대 높이
        answer.append(mid)
        start = mid+1
    else:
        end = mid-1
print(max(answer))


