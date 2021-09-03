def checkLen(pw):
    if len(pw) < 8:
        return True

def checkProp(pw):
    prop = [False,False,False,False]
    for i in range(len(pw)):
        if pw[i] in 'qwertyuiopasdfghjklzxcvbnm'.upper():
            prop[0] = True
        elif pw[i] in 'qwertyuiopasdfghjklzxcvbnm':
            prop[1] = True
        elif pw[i] in '1234567890':
            prop[2] = True
        else:
            prop[3] = True
    return prop
        
def checkSame4(pw):
    prev = ''
    count = 1
    for i in range(len(pw)):
        if pw[i] == prev:
            count += 1
            if count == 4:
                return True
        else:
            prev = pw[i]
            count = 1
    return False

def checkNumSeq(pw):
    numSeq = '0123456789012'
    revNumSeq = numSeq[::-1]
    for i in range(len(pw)-3):
        if pw[i:i+4] in numSeq or pw[i:i+4] in revNumSeq:
            return True
    return False

def checkLetSeq(pw):
    letSeq = 'abcdefghijklmnopqrstuvwxyzabc'
    revLetSeq = letSeq[::-1]
    for i in range(len(pw)-3):
        if pw[i:i+4].lower() in letSeq or pw[i:i+4].lower() in revLetSeq:
            return True
    return False

def checkKeyPat(pw):
    keyPat = ['!@#$%^&*()_+!@#','qwertyuiopqwe','asdfghjklasd','zxcvbnmzxc']
    revKeyPat = [i[::-1] for i in keyPat]
    for i in range(len(pw)-3):
        for j in range(len(keyPat)):
            if pw[i:i+4].lower() in keyPat[j] or pw[i:i+4].lower() in revKeyPat[j]:
                return True
    return False

pw = input()
isStrong = True

if checkLen(pw):
    print('Less than 8 characters')
    isStrong = False

prop = checkProp(pw)
if not prop[1]:
    print('No lowercase letters')
    isStrong = False
if not prop[0]:
    print('No uppercase letters')
    isStrong = False
if not prop[2]:
    print('No numbers')
    isStrong = False
if not prop[3]:
    print('No symbols')
    isStrong = False

if checkSame4(pw):
    print('Character repetition')
    isStrong = False

if checkNumSeq(pw):
    print('Number sequence')
    isStrong = False

if checkLetSeq(pw):
    print('Letter sequence')
    isStrong = False

if checkKeyPat(pw):
    print('Keyboard pattern')
    isStrong = False

if isStrong:
    print('OK')