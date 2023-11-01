N = input()

ans = 'Yes'

if len(N)>=2:
    for i in range(len(N)-1):
        a = int(N[i])
        b = int(N[i+1])

        if a<=b:
            ans = 'No'



print(ans) 