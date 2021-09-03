def no_lowercase(t): # return True if no lowercase, otherwise return False
    k = t
    for i in range(len(k)):
        if 'a'<=k[i]<='z' :
            return False
    return True
def no_uppercase(t):
    k = t
    for i in range(len(k)):
        if 'A'<=k[i]<='Z' :
            return False
    return True
def no_number(t):
    k = t
    for i in range(len(k)):
        if '0'<=k[i]<='9' :
            return False
    return True
def no_symbol(t):
    k = t
    for i in range(len(k)):
        if k[i] in ['!','@','#','$','%','^','&','*','(',')','_','+','"',"'",'=','-'] :
            return False
    return True
def character_repetition(t):
    for i in range(0,len(t)-3) :
            if t[i] == t[i+1] == t[i+2] == t[i+3] :
                return True
    return False
def number_sequence(t):
    for i in range(len(t)-3) :
        if '0' <= t[i] <= '9':
            if int(t[i+1])%10==(int(t[i])+1)%10 and int(t[i+2])%10==(int(t[i+1])+1)%10 and int(t[i+3])%10==(int(t[i+2])+1)%10 :
                return True
            if int(t[i+1])%10==(int(t[i])-1)%10 and int(t[i+2])%10==(int(t[i+1])-1)%10 and int(t[i+3])%10==(int(t[i+2])-1)%10 :
                return True
    return False
def letter_sequence(t):
    for i in range(len(t)-3) :
        k1 = ord(t[i]) ; k2 = ord(t[i+1]) ; k3 = ord(t[i+2]) ;k4 = ord(t[i+3])
        if 65 <= k1 <= 65+26 : k1-=65
        if 65 <= k2 <= 65+26 : k2-=65
        if 65 <= k3 <= 65+26 : k3-=65
        if 65 <= k4 <= 65+26 : k4-=65
        if 97 <= k1 <= 97+26 : k1-=97
        if 97 <= k2 <= 97+26 : k2-=97
        if 97 <= k3 <= 97+26 : k3-=97
        if 97 <= k4 <= 97+26 : k4-=97
        if (k4 == k3-1 == k2-2 == k1-3 or k4 == k3+1 == k2+2 == k1+3) and 0<=k1<=25 :
            return True
    return False
def keyboard_pattern(t):
    key1 = '!@#$%^&*()_+'
    key2 = 'QWERTYUIOP'
    key3 = 'ASDFGHJKL'
    key4 = 'ZXCVBNM'
    t = t.upper()
    for i in range(len(t)-3):
        if (t[i] in key1) and (t[i+1] in key1) and (t[i+2] in key1) and (t[i+3] in key1) :
            k1 = key1.index(t[i])
            k2 = key1.index(t[i+1])
            k3 = key1.index(t[i+2])
            k4 = key1.index(t[i+3])
            if k4 == k3-1 == k2-2 == k1-3 or k4 == k3+1 == k2+2 == k1+3 :
                return True
        if (t[i] in key2) and (t[i+1] in key2) and (t[i+2] in key2) and (t[i+3] in key2) :
            k1 = key2.index(t[i])
            k2 = key2.index(t[i+1])
            k3 = key2.index(t[i+2])
            k4 = key2.index(t[i+3])
            if k4 == k3-1 == k2-2 == k1-3 or k4 == k3+1 == k2+2 == k1+3 :
                return True
        if (t[i] in key3) and (t[i+1] in key3) and (t[i+2] in key3) and (t[i+3] in key3) :
            k1 = key3.index(t[i])
            k2 = key3.index(t[i+1])
            k3 = key3.index(t[i+2])
            k4 = key3.index(t[i+3])
            if k4 == k3-1 == k2-2 == k1-3 or k4 == k3+1 == k2+2 == k1+3 :
                return True
        if (t[i] in key4) and (t[i+1] in key4) and (t[i+2] in key4) and (t[i+3] in key4) :
            k1 = key4.index(t[i])
            k2 = key4.index(t[i+1])
            k3 = key4.index(t[i+2])
            k4 = key4.index(t[i+3])
            if k4 == k3-1 == k2-2 == k1-3 or k4 == k3+1 == k2+2 == k1+3 :
                return True
    return False

#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print("OK")
else:
    for i in errors:
        print(i)