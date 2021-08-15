# From the course "First steps in computing and python"
# 6.3.1

# The Func' is getting two arguments: 1 - is the text, 2 - is the number we want to move the letters

def caesar_encrypt(plaintext, offset):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char) # givinig the index of char in alphahbet
            # new index for the new char, that will mak it encrypted
            new_position = (position + offset) % 26
            # the index of the encrypted char
            new_char = alphabet[new_position]
            print(char, "-->", new_char) # We can track after the encrypted char
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            print(char, "unchanged")

    return ciphertext

print(caesar_encrypt("abc", 1))
print(caesar_encrypt("xyz", 1))
print(caesar_encrypt("hello", 10))
print(caesar_encrypt("Hello!!", 10))
print(caesar_encrypt("Hello!!", 36))
print(caesar_encrypt("Hello!!", -1))

# 6.3.4
# a practice question
# the answer is to change tje modulu from "%26" to "%len(alphabet)", because 26 is for english alphabet, and we want actualy the len of the 'alphabet string' because it can change depending on the language
# link: https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/e4908534f9904cd4b6ee0e51f1c99b21/19cce70af914478a8a093f4cbb520e58/?child=first

# Fix this function:
def modular_caesar_encrypt(plaintext, alphabet, offset):
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
###################################          # they did like this and there was an error which said "string index out of range" ##########
            # new_position = (position + offset) % 26
            new_position = (position + offset) % len(alphabet)
            new_char = alphabet[new_position]
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")
    return ciphertext

"""
### TESTS ###

import sol

print("********************")
print("Starting the test:")

print("********************")
alphabet = "!@#$%"
plaintext = "!!!"
offset = 1
print("Encrypting the following plaintext:", plaintext)
print("Using the following alphabet:", alphabet)
print("Using the following offset:", offset)
ans = caesar_encrypt(plaintext, alphabet, offset)
correct_ans = sol.caesar_encrypt(plaintext, alphabet, offset)
if ans == correct_ans:
    print("CORRECT: Very good, the encrypted text is:", correct_ans)
else:
    print("WRONG: The encrypted text should be:", correct_ans, ", but you got:", ans)

print("********************")
alphabet = "!@#$%"
plaintext = "!!!"
offset = 10
print("Encrypting the following plaintext:", plaintext)
print("Using the following alphabet:", alphabet)
print("Using the following offset:", offset)
ans = caesar_encrypt(plaintext, alphabet, offset)
correct_ans = sol.caesar_encrypt(plaintext, alphabet, offset)
if ans == correct_ans:
    print("CORRECT: Very good, the encrypted text is:", correct_ans)
else:
    print("WRONG: The encrypted text should be:", correct_ans, ", but you got:", ans)

print("********************")
alphabet = "abcdefghijklmnopqrstuvwxyz"
plaintext = "hello"
offset = 10
print("Encrypting the following plaintext:", plaintext)
print("Using the following alphabet:", alphabet)
print("Using the following offset:", offset)
ans = caesar_encrypt(plaintext, alphabet, offset)
correct_ans = sol.caesar_encrypt(plaintext, alphabet, offset)
if ans == correct_ans:
    print("CORRECT: Very good, the encrypted text is:", correct_ans)
else:
    print("WRONG: The encrypted text should be:", correct_ans, ", but you got:", ans)

print("********************")
alphabet = "QWERTY"
plaintext = "WE aRE ThE champions!"
offset = 123
print("Encrypting the following plaintext:", plaintext)
print("Using the following alphabet:", alphabet)
print("Using the following offset:", offset)
ans = caesar_encrypt(plaintext, alphabet, offset)
correct_ans = sol.caesar_encrypt(plaintext, alphabet, offset)
if ans == correct_ans:
    print("CORRECT: Very good, the encrypted text is:", correct_ans)
else:
    print("WRONG: The encrypted text should be:", correct_ans, ", but you got:", ans)

print("********************")
alphabet = "ONLY_BIG"
plaintext = "only small!"
offset = 12345
print("Encrypting the following plaintext:", plaintext)
print("Using the following alphabet:", alphabet)
print("Using the following offset:", offset)
ans = caesar_encrypt(plaintext, alphabet, offset)
correct_ans = sol.caesar_encrypt(plaintext, alphabet, offset)
if ans == correct_ans:
    print("CORRECT: Very good, the encrypted text is:", correct_ans)
else:
    print("WRONG: The encrypted text should be:", correct_ans, ", but you got:", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

"""

# decrypt 6.3.5
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/e4908534f9904cd4b6ee0e51f1c99b21/19cce70af914478a8a093f4cbb520e58/?child=first
# the video is important for understandig
# if you hva the offset key, the decrypt is very similar to the encrypt you are just going back with the same offset
# it is like you encrypting the encrypted text, but the oposite way, with a different offset which will return the text to original

def caesar_decrypt(ciphertext, offset):
    plaintext = caesar_encrypt(ciphertext, -offset)
    return plaintext

ciphertext = caesar_encrypt("hello", 10)
print("ciphertext:", ciphertext)
plaintext = caesar_decrypt(ciphertext, 10)
print("plaintext:", plaintext)

print()

# caesar break, 6.4.2

# here we will write a Func' that will break the ciphertext
# we just need to try all the offsets and to see with the eye if we getting any logical sentence in english
# for computer, trying 25 offsets (without 0 because it doesn't change anything) it is very simple

ciphertext = "iwxh xh iwt dgxvxcpa eapxcitmi"

# the regular encrypt
def caesar_encrypt(plaintext, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + offset) % 26
            new_char = alphabet[new_position]
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")

    return ciphertext

# the decrypt
def caesar_decrypt(ciphertext, offset):
    plaintext = caesar_encrypt(ciphertext, -offset)
    return plaintext

ciphertext = "iwxh xh iwt dgxvxcpa eapxcitmi"

######## the breaking of "caesar cipher" ########
def caesar_break(ciphertext):
    for offset in range(1, 26):
        maybe = caesar_decrypt(ciphertext, offset)
        print(offset, "-->", maybe)

caesar_break(ciphertext)
caesar_break("ps")