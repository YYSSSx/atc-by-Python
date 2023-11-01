N, T = map(str, input().split())
N = int(N)

K = 0
ans = []
for i in range(N):
    S = input()
    isOK = False
    if S == T:
        isOK = True
        
    elif len(T)+1 == len(S):
        for j in range(len(S)):
            if S[0:j]+S[j+1:len(S)]==T:
                isOK = True
                
    elif len(S)+1 == len(T):
        for k in range(len(T)):
            if T[0:k]+T[k+1:len(T)]==S:
                isOK = True
                
    elif len(S) == len(T):
        for l in range(len(S)):
            if S[0:l]+S[l+1:len(S)] == T[0:l]+T[l+1:len(T)]:
                isOK = True
        m=len(S)//2
        while True:
            if S[m+1:] != T[m+1:]:
                m+=m/2
            if S[:m] != T[:m]:
                m-=m/2

    if isOK == True:
        K += 1
        ans.append(i+1)

print(K)
print(*ans)