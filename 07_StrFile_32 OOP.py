class Password:
    def __init__(self,password):
        self.psw = password
        self.weak = []
    
    def __str__(self):
        formatString = ""
        for i in range(len(self.weak)):
            formatString += self.weak[i]
        return formatString

    def checker(self):
        self.checkLen()
    
    def checkLen(self):
        if len(self.psw) < 8:
            self.weak.append('Less than 8 characters')

    # def checkProp(self):
    #     prop = [False,False,False,False]
    #     for i in range(len(self.psw)):
    #         if self.psw[i] in 'qwertyuiopasdfghjklzxcvbnm'.upper():
    #             prop[0] = True
    #         elif self.psw[i] in 'qwertyuiopasdfghjklzxcvbnm':
    #             prop[1] = True
    #         elif self.psw[i] in '1234567890':
    #             prop[2] = True
    #         else:
    #             prop[3] = True
    #     return prop
            
    # def checkSame4(self):
    #     prev = ''
    #     count = 1
    #     for i in range(len(self.psw)):
    #         if self.psw[i] == prev:
    #             count += 1
    #             if count == 4:
    #                 return True
    #         else:
    #             prev = self.psw[i]
    #             count = 1
    #     return False

    # def checkNumSeq(self):
    #     numSeq = '0123456789012'
    #     revNumSeq = numSeq[::-1]
    #     for i in range(len(self.psw)-3):
    #         if self.psw[i:i+4] in numSeq or self.psw[i:i+4] in revNumSeq:
    #             return True
    #     return False

    # def checkLetSeq(self):
    #     letSeq = 'abcdefghijklmnopqrstuvwxyzabc'
    #     revLetSeq = letSeq[::-1]
    #     for i in range(len(self.psw)-3):
    #         if self.psw[i:i+4].lower() in letSeq or self.psw[i:i+4].lower() in revLetSeq:
    #             return True
    #     return False

    # def checkKeyPat(self):
    #     keyPat = ['!@#$%^&*()_+!@#','qwertyuiopqwe','asdfghjklasd','zxcvbnmzxc']
    #     revKeyPat = [i[::-1] for i in keyPat]
    #     # print(revKeyPat)
    #     for i in range(len(self.psw)-3):
    #         for j in range(len(keyPat)):
    #             if self.psw[i:i+4].lower() in keyPat[j] or self.psw[i:i+4].lower() in revKeyPat[j]:
    #                 return True
    #     return False


s = Password("123")
s.checker()
print(s)