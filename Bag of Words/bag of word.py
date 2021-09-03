with open('stopwords.txt') as f:
    data = f.readlines()
    stopword = []
    for i in range(len(data)):
        x = data[i].strip().split()
        for j in range(len(x)):
            stopword.append(x[j])

def fhash(w,M):
    G = 37
    res = 0
    for i in range(len(w)):
        res += ord(w[i].lower())*(37**(i))
    return res%M

word = "qwertyuiopasdfghjklzxcvbnm0123456789"

with open(input('File name = '),'r',encoding='utf8') as f:
    rawData = f.readlines()
    lineCount = len(rawData)
    for i in range(len(rawData)):
        rawData[i] = rawData[i].strip('\n')
    data = []
    for i in range(len(rawData)):
        if rawData[i] != "":
            data.append(rawData[i])
    # ---------------------------------
    charCount = 0
    alphaNum = 0
    wordCount = 0
    noStopWord = []
    # ---------------------------------
    for i in range(len(data)):
        # lineCount += 1
        for j in range(len(data[i])):
            if data[i][j].lower() in word:
                alphaNum += 1
            elif data[i][j].lower() not in word:
                if j == 0:
                    pass
                elif data[i][j-1] in word:
                    wordCount += 1
            charCount+=1
        if data[i][-1] in word:
            wordCount += 1
    # Remove Stop Word ---------------------------------
        w = data[i].split()
        for j in range(len(w)):
            if w[j].lower() not in stopword:
                noStopWord.append(w[j].lower())
    # -------------------------------------------------
    betterNoStopWord = []
    for i in range(len(noStopWord)):
        formatString = ""
        for j in range(len(noStopWord[i])):
            if noStopWord[i][j] in word:
                formatString += noStopWord[i][j]
        betterNoStopWord.append(formatString)
    # -------------------------------------------------
    bow = []
    useFhash = True
    M = 0
    while True:
        x = input("Use feature hashing ? (y,Y,n,N) ")
        if x in ['y','Y']:
            M = int(input("M = "))
            break
        elif x in ['n','N']:
            useFhash = False
            break
        else:
            print("Try again.")
    # -------------------------------------------------
    for i in range(len(betterNoStopWord)):
        if useFhash:
            for j in range(len(bow)):
                if bow[j][0] == fhash(betterNoStopWord[i],M):
                    bow[j][1] += 1
                    break
            else:
                bow.append([fhash(betterNoStopWord[i],M),1])

        else:
            for j in range(len(bow)):
                if bow[j][0] == betterNoStopWord[i]:
                    bow[j][1] += 1
                    break
            else:
                bow.append([betterNoStopWord[i],1])
    bow.sort()
    # -------------------------------------------------
    print("-------------------")
    print("char count =",charCount)
    print("alphanumeric count =",alphaNum)
    print("line count =",lineCount)
    print("word count =",wordCount)
    print("BoW =",bow)