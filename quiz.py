word = [i.strip() for i in input().split(',')]
correctName = []
for i in range(len(word)):
    name = ''
    for j in range(len(word[i])):
        if j == 0:
            name += word[i][j].upper()
        else:
            name += word[i][j].lower()
    correctName.append(name)

for i in range(len(correctName)):
    print(correctName[i],end=" ")