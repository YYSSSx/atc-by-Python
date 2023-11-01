s = input()

res = 'Yes'

flag1 = -1
flag2 = -1
flag3 = -1
flag4 = -1
flag5 = -1


for i in range(8):
    
    if s[i] == 'B':
        if flag1 == -1: flag1=i
        else :flag2 = i
    elif s[i] == 'R':
        if flag3 == -1: flag3=i
        else :flag4 = i

    if s[i] == 'K': flag5 = i

if flag1%2==flag2%2:
    res='No'
elif flag3>flag5 or flag5>flag4:
    res='No'

print(res) 
    