s = input()

op_cnt = len(s)-1

for i in range(2**op_cnt):
    op = ["-"] * op_cnt
    for j in range(op_cnt):
        if (i>>j)&1:
            op[op_cnt-1-j] = "+"
    
    res = ""
    for p_n, p_o in zip(s, op+[""]):
        res += p_n + p_o
    
    if eval(res) == 7:
        print(res+"=7")
        break
