import copy

N, X = map(int, input().split())

A = list(map(int, input().split()))

i = 0
ans =-1
for i in range(101):
    B = copy.copy(A)
    B.append(i)
    B.sort()
    a = sum(B) - B[0] - B[-1]
    if a>=X:
        ans = i
        break


print(ans)