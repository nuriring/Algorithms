#2차원 배열 회전 함수
def rotate(arr,M):
    new_arr = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_arr[j][M-1-i] = arr[i][j]
    return new_arr


#자물쇠 크기 세배로 늘리는 과정


#그리고 한칸씩 확인하는데 네방향 돌린걸 다 확인하면 넘어감

#
arr = [[0,1,1],[0,0,0],[0,0,0]]
print(rotate(arr,3))

# print(arr.count(1))
total = 0
for i in arr:
    total += i.count(1)
    # print(i.count(1))
print(total)

def check(arr):
    n = len(arr)//3
    for i in range(n,n*2):
        for j in range(n,n*2):
            if arr[i][j] != 1:
                return False
    return True

def solution(key,lock):
    answer = False
    M = len(key)
    N = len(lock)


    #0은 홈 #1은 돌기
    total = 0 #자물쇠 홈 총 갯수
    for i in lock:
        total += i.count(0)

    new_lock = [[0]*(3*N) for _ in range(3*N)]
    print(new_lock)
    for i in range(N,2*N):
        for j in range(N,2*N):
            new_lock[i][j] = lock[i%N][j%N]
    print(new_lock)
    cnt = 0
    rotate_cnt = 0
    for k in range(4):
        key = rotate(key,M)
        for i in range(3*N-M+1):
            for j in range(3*N-M+1):
                # key = rotate(key,M)
                # rotate_cnt += 1
                # if rotate_cnt == 4:
                #     rotate_cnt = 0
                #     continue
                for k in range(M):
                    for l in range(M):
                        new_lock[i+k][j+l] += key[k][l]
                if check(new_lock):
                    answer = True
                for k in range(M):
                    for l in range(M):
                        new_lock[i+k][j+l] -= key[k][l]




    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))




#2차원 배열 회전 함수
def rotate(arr,M):
    new_arr = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_arr[j][M-1-i] = arr[i][j]
    return new_arr

#자물쇠 풀렸는지 체크 함수
def check(arr):
    n = len(arr)//3
    for i in range(n,n*2):
        for j in range(n,n*2):
            if arr[i][j] != 1:
                return False
    return True

def solution(key,lock):
    answer = False
    M = len(key)
    N = len(lock)


    #0은 홈 #1은 돌기
    total = 0 #자물쇠 홈 총 갯수
    for i in lock:
        total += i.count(0)

    new_lock = [[0]*(3*N) for _ in range(3*N)]
    print(new_lock)
    for i in range(N,2*N):
        for j in range(N,2*N):
            new_lock[i][j] = lock[i%N][j%N]
    print(new_lock)
    cnt = 0
    rotate_cnt = 0
    #총 4번 회전
    for k in range(4):
        key = rotate(key,M)
        for i in range(3*N-M+1):
            for j in range(3*N-M+1):
                # key = rotate(key,M)
                # rotate_cnt += 1
                # if rotate_cnt == 4:
                #     rotate_cnt = 0
                #     continue
                #열쇠 끼워서 확인
                for k in range(M):
                    for l in range(M):
                        new_lock[i+k][j+l] += key[k][l]
                #자물쇠 풀리는지 체크
                if check(new_lock):
                    answer = True
                #자물쇠 자체에 변경을 가하고 있기 때문에
                #안됐으면 다시 열쇠 빼줌
                for k in range(M):
                    for l in range(M):
                        new_lock[i+k][j+l] -= key[k][l]




    return answer


    