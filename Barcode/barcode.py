# Prog-07: EAN-13 Barcode
# ??3?????21 Name ?

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):       
    x = [[int(e) for e in ean13_code]]         
    plt.axis('off')    
    plt.imshow(x, aspect='auto', cmap='binary')   
    plt.title(digits) 
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')  
    codes = encode_EAN13(digits)
    if codes == '':         
        print(digits, 'is not an EAN-13 number.')   
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------

L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================

def codes_of(digits, patterns):
    number = ""
    for i in range(len(digits)):
        if patterns[i] == "L":
            number += L_codes[int(digits[i])]
        elif patterns[i] == "G":
            number += G_codes[int(digits[i])]
        else:
            number += R_codes[int(digits[i])]
    return number

def digits_of(codes):
    digit = ""
    for i in range(0,len(codes),7):
        x = codes[i:i+7]
        if x in L_codes:
            digit += str(L_codes.index(x))
        elif x in G_codes:
            digit += str(G_codes.index(x))
        elif x in R_codes:
            digit += str(R_codes.index(x))
        else:
            return ""
    return digit

def patterns_of(codes):
    pattern = ""
    for i in range(0,len(codes),7):
        x = codes[i:i+7]
        if x in L_codes:
            pattern += "L"
        elif x in G_codes:
            pattern += "G"
        elif x in R_codes:
            pattern += "R"
        else:
            return ""
    return pattern

def check_digit(digits):
    sumDigit = 0
    for i in range(len(digits)):
        if digits[i] not in '0123456789':
            return ''
    for i in range(len(digits)):
        if i%2==0:
            sumDigit += int(digits[i])
        else:
            sumDigit += int(digits[i])*3
    n = 0
    while n < sumDigit:
        n += 10
    check = n - sumDigit
    return check

def encode_EAN13(digits):
    barcodePattern = ['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']
    if len(digits)!=13 or str(check_digit(digits[:-1]))!=str(digits[12]):
        return ""
    
    return "101" + codes_of(digits[1:7],barcodePattern[int(digits[0])]) + "01010" + codes_of(digits[7:],"RRRRRR") + "101"

def decode_EAN13(codes):
    if len(codes) != 95:
        return ""
    barcodePattern = ['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']
    code1 = codes[3:45]
    code2 = codes[50:92]
    # ==============================================================
    barcode = ""
    if patterns_of(code1) not in barcodePattern:
        return ""
    barcode += str(barcodePattern.index(patterns_of(code1)))
    barcode += digits_of(code1)
    barcode += digits_of(code2)
    return barcode

#-------------------------------------------------
test1()