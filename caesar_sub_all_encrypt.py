# From the course: "first steps in computering and python", test number 6
# Question number 5

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


def caesar_decrypt(ciphertext, offset):
    plaintext = caesar_encrypt(ciphertext, -offset)
    return plaintext


def caesar_break(ciphertext):
    for offset in range(1, 26):
        maybe = caesar_decrypt(ciphertext, offset)
        print(offset, "-->", maybe)


def sub_encrypt(plaintext, alphabet, shuffled):
    ciphertext = ""

    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = shuffled[position]
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")

    return ciphertext


def sub_decrypt(ciphertext, alphabet, shuffled):
    plaintext = sub_encrypt(ciphertext, shuffled, alphabet)
    return plaintext


alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "icghkxpwstujzdleqmbvofanry"
cipher = "lahopka jp opkwzjat uoiaxoa"

ciphertext = sub_decrypt(cipher, alphabet, shuffled)
print(ciphertext)
caesar_break(ciphertext)

msg1 = caesar_encrypt(caesar_encrypt("abc", 5), -5)
msg2 = caesar_decrypt(caesar_encrypt("abc", 5), 4)
print(msg1)
print(msg2)

# Question number 10
# the Func' for the answer:
def caesar_break(cipher):
    popular_words = [' the ', ' for ', ' to ', ' of ', ' and ', ' yes ', ' i ', ' you ']

    for k in range(0, 25):
        maybe = caesar_decrypt(cipher, k)
        # print(maybe)
        for word in popular_words: # another loop to check if we have a popular word in the decrypt sentence
            if word in maybe:
                return maybe
    else:
        return ""


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Breaking 'zu hk ux tuz zu hk'")
ans = caesar_break('zu hk ux tuz zu hk')
if ans == 'to be or not to be':
    print("CORRECT: 'zu hk ux tuz zu hk' was originally 'to be or not to be'")
else:
    print("WRONG: 'zu hk ux tuz zu hk' was originally 'to be or not to be' but your code returned", ans)

print("********************")
print("Breaking 'uhx c qcff ufqusm fipy sio'")
ans = caesar_break('uhx c qcff ufqusm fipy sio')
if ans == 'and i will always love you':
    print("CORRECT: 'uhx c qcff ufqusm fipy sio' was originally 'and i will always love you'")
else:
    print("WRONG: 'uhx c qcff ufqusm fipy sio' was originally 'and i will always love you' but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

