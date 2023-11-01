K = int(input())
A = [0]*10
flag = 0
while(K>=flag):
    for i in range(10):
        for j in range(i, 10):
            A[i] = A[i]+1
            flag += 1
            if flag == K:
                ans = A[9]*10000000000+A[8]*100000000+A[7]*10000000+A[6]*1000000+A[5]*100000+A[4]*10000+A[3]*1000+A[2]*100+A[1]*10+A[0]

print(ans)
    