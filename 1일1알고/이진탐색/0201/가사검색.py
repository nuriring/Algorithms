# from bisect import bisect_left,bisect_right
# arr = [3,3,3,4,4]
#
# # arr = [2,2,3,3,3]
# print(bisect_left(arr,4))
# print(bisect_right(arr,4))
import sys

sys.setrecursionlimit(10 ** 7)
arr = '????' #이케이스만 예외처리



# ?와 글자가 함께 있을때 ?위치찾는 함수
def binary_search(arr, start, end):
    #예외처리
    if len(arr)<=2 and arr[-1]=='?':
        return 1
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[-1] == '?' and (mid == 0 or arr[mid - 1] != '?') and arr[mid] == '?':
        return mid
    elif arr[0] == '?' and (mid == len(arr) - 1 or arr[mid + 1] != '?') and arr[mid] == '?':
        return mid
    elif arr[-1] == '?' and arr[mid - 1] == '?':
        return binary_search(arr, start, mid)
    elif arr[-1] == '?' and arr[mid - 1] != '?':
        return binary_search(arr, mid + 1, end)
    elif arr[0] == '?' and arr[mid + 1] == '?':
        return binary_search(arr, mid + 1, end)
    elif arr[0] == '?' and arr[mid + 1] != '?':
        return binary_search(arr, start, mid)



print(binary_search(arr, 0, len(arr) - 1))
print(arr.count('?'))


# ?와 글자가 함께 있을때 ?위치찾는 함수
def binary_search(arr, start, end):
    # 예외처리
    if len(arr) <= 2 and arr[-1] == '?':
        return 1
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[-1] == '?' and (mid == 0 or arr[mid - 1] != '?') and arr[mid] == '?':
        return mid
    elif arr[0] == '?' and (mid == len(arr) - 1 or arr[mid + 1] != '?') and arr[mid] == '?':
        return mid
    elif arr[-1] == '?' and arr[mid - 1] == '?':
        return binary_search(arr, start, mid)
    elif arr[-1] == '?' and arr[mid - 1] != '?':
        return binary_search(arr, mid + 1, end)
    elif arr[0] == '?' and arr[mid + 1] == '?':
        return binary_search(arr, mid + 1, end)
    elif arr[0] == '?' and arr[mid + 1] != '?':
        return binary_search(arr, start, mid)


def solution(words, queries):
    answer = []
    for query in queries:
        print(binary_search(query, 0, len(query) - 1))
        cnt = 0
        for word in words:
            if query.count('?') == len(query):  # 전부다 물음표일 때
                if len(word) == len(query):  # 글자수만 같으면 동일
                    cnt += 1
            else:  # 물음표랑 글자랑 섞여있을때
                pointer = binary_search(query, 0, len(query) - 1)
                # ?가 접미사일 때
                if query[-1] == '?':
                    if len(word) == len(query) and word[0:pointer] == query[0:pointer]:
                        cnt += 1
                # 접두사일 때
                else:
                    if len(word) == len(query) and word[pointer + 1:len(word)] == query[pointer + 1:len(word)]:
                        cnt += 1

        answer.append(cnt)
    return answer