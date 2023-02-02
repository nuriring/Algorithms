# def solution(s):
#     res = len(s)
#     letter = ''
#
#     for i in range(1, len(s) // 2 + 1):
#         cnt = 1
#         answer = ''
#         flag = False
#         for j in range(0, len(s), i):
#
#             if s[j:j+i] == s[j+i:j+(2*i)]:
#                 flag=True
#                 letter = s[j:j+i]
#                 cnt += 1
#                 continue
#             else:
#                 if not flag:
#                     answer += s[j:j+i]
#
#             if cnt>1:
#
#                 answer += (str(cnt)+letter)
#                 letter = ''
#                 cnt = 1
#                 flag = False
#         if res > len(answer):
#             res = len(answer)
#     return res



def solution(s):
    answer = len(s)
    #1개 단위 step 부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2+1):
        compressed = ''
        prev = s[0:step] #앞에서부터 step만큼의 문자열 추출
        count = 1
        for j in range(step, len(s), step):
            #이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j+step]:
                count += 1
            else:
                # 다른 문자열이 나왔다면 더이상 압축 x
                #A if 조건 else B
                #조건값이 True(참)이면 A를 False(거짓)이면 B를 반환
                compressed += str(count) + prev if count >=2 else prev
                #다시 상태 초기화
                prev = s[j:j+step]
                count = 1
        #남아있는 문자열에 대한 처리
        compressed += str(count) + prev if count >=2 else prev
        answer = min(answer,len(compressed))
    return answer

print(solution('ababcccab'))