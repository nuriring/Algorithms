


#이미 균형잡힌 괄호 문자열이 주어지고 있음
def devide(sentence):
    open = 0
    close = 0
    for i in range(len(sentence)):
        if sentence[i] =='(':
            open +=1
        else:
            close += 1
        if open==close:
            return sentence[0:i+1], sentence[i+1:]

# def right(sentence):
#     stack = []
#     stack.append(sentence[0])
#     for i in sentence[1:]:
#         if stack and i == '(' and stack[-1] == ')':
#             stack.pop()
#         elif stack and i == ')' and stack[-1] == '(':
#             stack.pop()
#         elif not stack and i == ')':
#             # 스택이 비어있는데 닫는게 나오면 이미 잘못된 괄호니까
#             return False
#         else:
#             stack.append(i)
#     if len(stack) == 0:
#         return True
#     return False



def solution(p):
    answer = ''
    if len(p) == 0:
        return answer

    u,v = devide(p)
    if right(u):
        tmp = solution(v)
        return u+tmp

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for j in u[1:len(u) - 1]:
            if j == '(':
                answer += ')'
            else:
                answer += '('
        return answer