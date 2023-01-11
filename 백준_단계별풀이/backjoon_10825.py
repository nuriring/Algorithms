import sys
sys.stdin = open('10825.txt', 'r')

# 국영수 순으로 정렬
T = int(input())
score = []
for tc in range(T):
    score.append(list(input().split()))
    # print(score)
# print(score)
sorted_list = sorted(score, key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in sorted_list:
    # print(i)
    print(i[0])

    # print(sorted_list)
