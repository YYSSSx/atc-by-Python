N = int(input())
S = []
for i in range(N):
    S.append(list(input()))

pre_ans = [0]*N
for j in range(N):
    for k in range(N):
        if S[j][k] =='o':
            pre_ans[j] += 1

for i in reversed(range(max(pre_ans)+1)):
    for j in range(N):
        if i==pre_ans[j]:
            print(j+1)


