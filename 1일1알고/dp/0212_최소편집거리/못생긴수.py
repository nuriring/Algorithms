#오직 2,3,5 만 약수
#1포함
#n번쨰 못생긴수
#dp를 어디다 써야하지
#사실 1000까지면
#하나씩
#n번째 못생긴수
# 2  3  22  5   23  222  33  25   223
# n = int(input())
# #못생긴 수를 담기위한 테이블 1차원 dp
# ugly = [0]*n
# ugly[0] = 1
#
# #2배, 3배, 5배를 위한 인덱스
# i2 = i3 = i5 = 0
#
# #처음에 곱샘값을 초기화
# next2, next3, next5 = 2, 3, 5

#1부터 n까지 못생긴 수를 찾기



def game():
    n = 10
    # 못생긴 수를 담기위한 테이블 1차원 dp
    ugly = [0] * n
    ugly[0] = 1

    # 2배, 3배, 5배를 위한 인덱스
    i2 = i3 = i5 = 0

    # 처음에 곱샘값을 초기화
    next2, next3, next5 = 2, 3, 5
    for k in range(1, n):
        # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
        ugly[k] = min(next2, next3, next5)

        # 인덱스에 따라서 곱셈 결과를 증가
        # 인덱스를 증가시켜서 2,3,5로 곱해지는 값들을 구할 수 있음
        if ugly[k] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[k] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[k] == next5:
            i5 += 1
            next5 = ugly[i5] * 5




game()

