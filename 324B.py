N = int(input())

ans='No'
for i in range(61):
    for j in range(40):
        if N==2**i * 3**j:
            ans = 'Yes'

print(ans)