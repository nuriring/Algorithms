N = int(input())
nums = list(map(int,input().split()))
dp = [nums[0]]
for i in nums[1:]:
    dp.append(max(i,dp[-1]+i)) #음수일때는 dp[-1]값이 다음 양수 값보다 작아지니까 다음 양수 값으로 대체되서 연속합이 새로 시작되는 원리를 이용


print(max(dp))