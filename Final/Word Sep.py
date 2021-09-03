with open("input.txt") as f:
    data = [i.strip() for i in f.readlines()]

upperText = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "0123456789"

splitText = []
for i in range(len(data)):
    startInd = 0
    subSplitText = []
    isNumber = False
    for j in range(len(data[i])):
        if not isNumber:
            if data[i][j] in upperText:
                subSplitText.append(data[i][startInd:j])
                startInd = j
            elif data[i][j] in number:
                subSplitText.append(data[i][startInd:j])
                startInd = j
                isNumber = True
        if isNumber:
            if data[i][j] not in number:
                subSplitText.append(data[i][startInd:j])
                startInd = j
                isNumber = False
    subSplitText.append(data[i][startInd:j+1])
    subSplitText = [i for i in subSplitText if i!=""]
    splitText.append(subSplitText)

with open("output.txt","w") as f:
    for i in range(len(splitText)):
        for j in range(len(splitText[i])):
            if j == len(splitText[i])-1:
                f.write(splitText[i][j])
            else:
                f.write(splitText[i][j]+" ,")
        f.write('\n')
