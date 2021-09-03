def continued_frac(A):
    res = []
    for i in range(len(A)):
        if i==0:
            res.append(A[0])
        else:
            subRes = A[i-1]+1/A[i]
            for j in range(i,-1,-1):
                subRes = A[j]+1/subRes
            res.append(subRes)
    print(res)

continued_frac([1,8,7,9])