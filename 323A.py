S = input()
ans = 'Yes'
for i in range(16):
    if i%2==1 and S[i]=='1':
        ans = 'No'
        break

print(ans)