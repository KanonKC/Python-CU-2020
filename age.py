a = input().split()
b = input().split()

nA = a[0]
nB = b[0]
dateA = a[1].split("/")
dateB = b[1].split("/")

dA = int(dateA[0])
mA = int(dateA[1])
yA = int(dateA[2])
dB = int(dateB[0])
mB = int(dateB[1])
yB = int(dateB[2])

if yB > yA:
    print(nA)
elif yB < yA:
    print(nB)
else:
    if mB > mA:
        print(nA)
    elif mB < mA:
        print(nB)
    else:
        if dB > dA:
            print(nA)
        elif dB < dA:
            print(nB)
        else:
            print(nA,nB)