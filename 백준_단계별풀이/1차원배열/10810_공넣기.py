N,M = map(int,input().split())
basket = [0]
for i in range(1,N+1):
    basket.append(i)
# print(basket)
for _ in range(M):
    i,j = map(int,input().split())
    if i!=j:
        rev = [0]+list(reversed(basket[i:j+1]))
        # print(rev)

        for idx in range(i,j+1):
            basket[idx] = rev[idx-i+1]
    else:
        continue

print(*basket[1:])




