# Prog-10: Steganography
# 6?3?????21 Name ?

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename):       
    im = Image.open(filename).convert('RGB')         
    return numpy.asarray(im).tolist()    
   
def save_image(img, filename): 
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
  
def show_image(filename):
    im = Image.open(filename)         
    im.show()   

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------

def decToBi(dec):
    bi = ""
    while dec > 0:
        bi = str(dec%2) + bi
        dec //= 2
    return bi
    
def biToDec(bi):
    bi = str(bi)
    dec = 0
    for i in range(len(bi)):
        dec += int(bi[i])*(2**(len(bi)-1-i))
    return dec

# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    imgMat = load_image(file_in)
    # print(imgMat)
    pixel = len(imgMat)*len(imgMat[0])
    if (len(text)*8)/3+16 <= pixel:
        bit = "0100111101001011"

        wordLen = str(decToBi(len(text)))
        while len(wordLen) < 16:
            wordLen = "0"+wordLen
        bit += wordLen

        for i in range(len(text)):
            bit += char_to_bits(text[i])

        bit += "0100111101001011"

        print(bit)
        
        b = 0
        for i in range(len(imgMat)):
            for j in range(len(imgMat[i])):
                for k in range(len(imgMat[i][j])):
                    pix = imgMat[i][j][k]
                    if pix % 2 == 0 and bit[b] == "1":
                        imgMat[i][j][k] += 1
                    elif pix % 2 != 0 and bit[b] == "0":
                        imgMat[i][j][k] -= 1
                    b += 1
                    if b == len(bit):
                        # print(imgMat)
                        save_image(imgMat,file_out)
                        return True
    return False

# --------------------------------------------------

def get_embedded_text_from_image(file_in):
    imgMat = load_image(file_in)
    # print(imgMat)
    bit = ""
    for i in range(len(imgMat)):
        for j in range(len(imgMat[i])):
            for k in range(len(imgMat[i][j])):
                if imgMat[i][j][k] % 2 == 0:
                    bit += "0"
                else:
                    bit += "1"

    specialBit = bit[:16]
    lenBit = int(biToDec(int(bit[16:32])))
    endOfStringBit = 32+(lenBit*8)
    stringBit = bit[32:endOfStringBit]
    endSpecialBit = bit[endOfStringBit:endOfStringBit+16]
    
    char = ""
    if specialBit == endSpecialBit:
        for i in range(0,len(stringBit),8):
            char += bits_to_char(stringBit[i:i+8])
        return char
    else:
        return ""

# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
# main()
print(load_image("5x5_A.png"))

