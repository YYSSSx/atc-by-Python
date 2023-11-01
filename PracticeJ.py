s = input()

index = 0
flag1 = True
w = ['maerd', 'remaerd', 'esare', 'resare' ]

s = s[::-1]

while index != len(s):

    flag2 = False
    
    for i in w:
        if s[index:index+len(i)] == i:
            index += len(i)
            flag2 = True
    
    if flag2 == False:
        flag1 = False
        break

        
if flag1 == True:
    print('YES')
else:
    print('NO')
