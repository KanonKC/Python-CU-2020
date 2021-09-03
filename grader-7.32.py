password = input().strip()
def one(password,count): #check if pass length longer than 8
    if len(password) < 8 :
        print('Less than 8 characters')
        count += 1
    return count

def two(password,count): #check if have upper case and lower case
    up,low,sym,num = 0,0,0,0
    for e in password:
        if e.isupper() : up += 1
        if e.islower() : low += 1
        if e in '0123456789': num += 1
        if e in '\'"()[]{}=+-_*&^%$#@!/\\,.<>?;:' : sym += 1;
    if (up == 0) or (low == 0) or (num == 0) or (sym == 0):
        if low == 0: print('No lowercase letters')
        if up  == 0: print('No uppercase letters')
        if num == 0: print('No numbers')
        if sym == 0: print('No symbols')
        count += 1
    return count

def three(password,count): #ไม่มี 4 ตัวติิดกัน
    for i in range(len(password)-3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            print('Character repetition')
            count += 1
            return count
    return count

def four(password,count):
    p = str(password).lower() #password copy
    a = '0123456789012'
    b = 'abcdefghijklmnopqrstuvwxyzabc'
    c = '!@#$%^&*()_+!@#'
    d = 'qwertyuiopqwe'
    e = 'asdfghjklasd'
    f = 'zxcvbnmzxc'
    g,h,j = 0,0,0
    for i in range(len(password)-3):
        if (p[i:i+4] in a) or (p[i:i+4][::-1] in a): g += 1
        if (p[i:i+4] in b) or (p[i:i+4][::-1] in b): h += 1
        if (p[i:i+4] in c) or (p[i:i+4][::-1] in c): j += 1
        if (p[i:i+4] in d) or (p[i:i+4][::-1] in d): j += 1
        if (p[i:i+4] in e) or (p[i:i+4][::-1] in e): j += 1
        if (p[i:i+4] in f) or (p[i:i+4][::-1] in f): j += 1
    if g>0 or h>0 or j>0:
        if g>0 : print('Number sequence')
        if h>0 : print('Letter sequence')
        if j>0 : print('Keyboard pattern')
        count += 1
    return count   
#------------------------------------------------------------------------------
def main():
    count = 0
    count = one(password,count)
    count = two(password,count)
    count = three(password,count)
    count = four(password,count)    
    if count == 0: print('OK')
#------------------------------------------------------------------------------
main()
    
    
    
    
    
    
    