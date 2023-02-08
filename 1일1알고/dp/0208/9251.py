# test = 'abca'
# print(test.index('a'))

# N = int(input())  # 6
arr1 = list(input())
arr2 = list(input())



print(arr1)
print(arr2)
dp = [1] * (max(len(arr1),len(arr2)))
# 대상이 되는 문자열을 뒤집어서 index 조회했을 때
# index 값이 더 작으면 이후에 있다는 의미

arr2.reverse()
for i in range(len(arr1)):
    for j in range(i):
        #i가 뒤에 위치한값

        if arr2.index(arr1[i]) < arr2.index(arr1[j]):
            dp[i] = max(dp[j] + 1, dp[i])

print(dp)
#         if arr[i] > arr[j]:
#
#             #해당자리의 숫자를 해당자리 이전까지의 숫자와 싹다 비교하면서 더 작은 숫자가 있는 수만큼 누적되면서 길이가 담김
#             dp[i] = max(dp[j] + 1, dp[i])
#
# print(dp)
# x = max(dp)
# result = []
# for i in range(N-1,-1,-1):
#     #거꾸로 순회하면서 max(dp)값이랑 dp에서 값이 같을 때에 해당하는 index의 값을 arr에서찾아주면 그게 가장 긴 증가하는 수열의 최댓값
#     if dp[i] == x:
#         result.append(arr[i])
#         x -= 1 #거기서 부터 길이 한개씩 줄이면서 추가해주면 큰 수부터 차례대로 들어감
# result.reverse() #그걸 뒤집으면 수열 자체를 구할 수 있음
# print(max(dp))
# print(*result)