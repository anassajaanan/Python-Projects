import math
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
restart="yes"
while restart=="yes":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = (input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    if shift>25:
        shift=shift%26
        print(shift)
    if direction == "decode":
        shift*=-1
    def caesar_cipher(t,s,d):
        cipher_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_char = alphabet[new_position]
                cipher_text += new_char
            else:
                cipher_text += char
        return cipher_text
    print(caesar_cipher(text,shift,direction))
    restart=input('type "yes" if you want to go again, otherwise type "no"   ')
if restart=="no":
    print("Goodbye")


