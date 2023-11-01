import copy
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = []

for i in range(N):
    S.append(list(input()))

now = [0]*N
for i in range(N):
    now[i]+=i+1
    for j in range(M):
        if S[i][j] == 'o':
            now[i] += A[j]


max = max(now)

for i in range(N):
    r = []
    for j in range(M):
        if S[i][j] == 'x':
            r.append(A[j])
    r.sort(reverse=True)
    next = now[i]
    ans = 0
    while next<max:
        next+=r.pop(0)
        ans += 1
    print(ans)





