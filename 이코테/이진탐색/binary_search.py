#이진 탐색 구현(재귀)
def binary_search(array, target, start, end):
    if start>end:
        return None #타겟을 찾을 수 없음
    mid = (start+end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)



#이진탐색구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None
