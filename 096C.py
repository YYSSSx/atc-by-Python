h, w = map(int, input().split())

s = [input() for _ in range(h)]

res = 'No'
can1 = True

for i in range(h):
    for j in range(w):
        can2 = False
        if s[i][j] == '#':
            for k in range(-1, 2, 2):
                if i+k>=0 and i+k<h and s[i+k][j]=='#': 
                    can2 = True
                    break
                elif j+k>=0 and j+k<w and s[i][j+k]=='#': 
                    can2 = True
                    break

            if can2==False:
                can1 = False

if can1==True:
    res = 'Yes'

print(res)