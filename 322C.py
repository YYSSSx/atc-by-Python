N, M = map(int, input().split())
A = list(map(int, input().split()))

ind = M-1
ans = [1]*N
for i in reversed(range(N)):
    if i+1==A[ind]:
        ans[i]=0
        ind -= 1
    else:
        ans[i]=ans[i+1]+1

for i in ans:
    print(i)
