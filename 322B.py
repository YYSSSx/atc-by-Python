N, M = map(int, input().split())
S = input()
T = input()


ans = 3

if S==T[0:N]:
    ans = 1

if S==T[len(T)-len(S):M]:
    if ans==1:
        ans=0
    else:
        ans=2


print(ans)

