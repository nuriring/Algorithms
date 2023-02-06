N = int(input())  # 6
arr = list(map(int, input().split()))
dp1 = [1] * (N)
dp2 = [1] * (N)
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            # arr[i] = arr[j]
            #해당자리의 숫자를 해당자리 이전까지의 숫자와 싹다 비교하면서 더 작은 숫자가 있는 수만큼 누적되면서 길이가 담김
            dp1[i] = max(dp1[j] + 1, dp1[i])

arr.reverse()
# print(arr)
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            # arr[i] = arr[j]
            # 해당자리의 숫자를 해당자리 이전까지의 숫자와 싹다 비교하면서 더 작은 숫자가 있는 수만큼 누적되면서 길이가 담김
            dp2[i] = max(dp2[j] + 1, dp2[i])

# print(dp1,dp2)

#이렇게 더해주면 가장길게 증가하는 수열과 가장길게 감소하는 수열이 특정 i 기점으로 만나므로 최대 길이를 구할 수 있음

tmp_arr = [0]*(N)
for i in range(N):
    tmp_arr[i] = dp1[i] + dp2[::-1][i]
print(max(tmp_arr)-1)



#[1, 2, 2, 1, 3, 3, 4, 5, 2, 1] [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]
#[0, 1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
#[4, 3, 0, 1, 2, 1, 2, 1, 0, 0, 0]


# N = int(input())
#
# List = list(map(int, input().split()))
#
# dp1 = [1]*N
# dp2 = [1]*N
#
# sub_len=[0]*N
#
# Max=0
#
# for i in range(N):
#     for j in range(i):
#         if List[i] > List[j]:
#             dp1[i] = max(dp1[i], dp1[j]+1)
#
# List.reverse()
#
# for i in range(N):
#     for j in range(i):
#         if List[i]>List[j]:
#             dp2[i]=max(dp2[i],dp2[j]+1)
# dp2.reverse()
#
# print(dp1,dp2)
# for i in range(N):
#     sub_len[i]=dp1[i]+dp2[i]
#
# print(max(sub_len)-1)