import sys
input = sys.stdin.readline
N = int(input())
people = []
for i in range(N):
    age,name = input().split()
    people.append((age,name))
people.sort(key=lambda x:int(x[0]))
# print(people)
for i in people:
    print(*i)