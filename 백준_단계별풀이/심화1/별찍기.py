while True:
    N = int(input())
    if N == -1 :
        break
    cnt = 0
    nums = []
    for i in range(1,N):
        if N%i==0:
            nums.append(str(i))
            nums.append('+')
            cnt+=i
    if cnt==N:

        res = nums[0:len(nums)-1]
        ans = ' '.join(res)
        print(f'{N} = {ans}')
    else:
        print(f'{N} is NOT perfect.')