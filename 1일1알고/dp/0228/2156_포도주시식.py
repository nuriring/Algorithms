#포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고
#마신 후에는 원래 위치에 다시 놓아야 한다
#연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
#될수있는대로 많이



#연속횟수가 3미만이다
#먹는다 횟수늘린다
#내가 이걸 먹는게 이득이다
#아니다
n = int(input())
grape = [0]*n
d = [0]*n
for i in range(n):
    grape[i] = int(input())


d[0] = grape[0]
d[1] = grape[0]+grape[1]

d[2] = max(grape[2]+grape[0], grape[2]+grape[1], d[1]) #(전전전까지 최대양 + 한칸띄우고 + 현재양, 전전까지 최대양 + 이어서 현재양, 현재꺼 안먹는 경우)

#연속횟수가 3이상이다
#못먹는다 넘어간다 횟수초기화한다
for i in range(3,n):
    d[i] = max(grape[i]+d[i-2], grape[i]+grape[i-1]+d[i-3], d[i-1])

print(max(d))