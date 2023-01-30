from itertools import permutations
#취약지점은 오름차순으로 들어옴
def solution(n,weak,dist):
    # dist.sort(reverse=True)
    #가장 멀리까지 이동할 수 있는 친구를 먼저 투입
    #가장 먼거리를 먼저 해결해야함
    #1,5,6,10,13,18,22
    # 1 2 3 4
    # 1 3 2 4
    #완전 탐색
    # weak
    answer = len(dist)+1
    line_weak = weak[:]
    for i in weak:
        line_weak.append(i+n)
        # print(i)
    print(line_weak)
    perm = permutations(dist,len(dist))
    print(list(perm))
    for start in range(len(weak)):
        for friends in list(permutations(dist,len(dist))):
            #친구투입순서 순열 바뀜
            #케이스바뀔때마다 초기에는 한명
            count = 1
            #현재 투입된 친구가 점검할 수 있는 위치
            position = line_weak[start]+friends[count-1]
            for i in range(start, start+len(weak)):
                #취약지점 싹다 돌면서 현재친구의 위치로 점검이 다 가능한지 싹다 혹인
                if position<line_weak[i]:#현재 위치보다 큰 값이 있으면 더 투입
                    count += 1
                    if count > len(dist):
                        break #아무리투입해도 고칠수 없음
                    position = line_weak[i] + friends[count-1] #점검가능한 위치만큼 이동시킨 후 더 확인
            answer = min(count,answer)

    if answer>len(dist):
        return -1
    return answer




n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]


print(solution(n,weak,dist))
