# From the course: "first steps in computering and python", test number 6
# Question number 7

# Actually it is a private case of substitution encryp, but it is a special way by it self

def sub_encrypt(plaintext, alphabet, shuffled):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = shuffled[position]
            #   print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
        #  print(char, "unchanged")

    return ciphertext


def encrypt_atbash(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shuffled = "zyxwvutsrqponmlkjihgfedcba"
    # shuffled = ""
    # for i in range(len(alphabet),0,-1):
    #    shuffled += i

    new_msg = sub_encrypt(msg, alphabet, shuffled)
    return new_msg


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Encrypting 'hello world'")
ans = encrypt_atbash('hello world')
if ans == 'svool dliow':
    print("CORRECT: 'hello world' is encrypted by atbash to 'svool dliow'")
else:
    print("WRONG: 'hello world' is encrypted by atbash to 'svool dliow' but your code returned", ans)

print("********************")
print("Encrypting 'abcdefghijklmnopqrstuvwxyz'")
ans = encrypt_atbash('abcdefghijklmnopqrstuvwxyz')
if ans == 'zyxwvutsrqponmlkjihgfedcba':
    print("CORRECT: 'abcdefghijklmnopqrstuvwxyz' is encrypted by atbash to 'zyxwvutsrqponmlkjihgfedcba'")
else:
    print(
        "WRONG: 'abcdefghijklmnopqrstuvwxyz' is encrypted by atbash to 'zyxwvutsrqponmlkjihgfedcba' but your code returned",
        ans)

print("********************")
print("Encrypting 'HELLO WORLD'")
ans = encrypt_atbash('HELLO WORLD')
if ans == 'HELLO WORLD':
    print("CORRECT: 'HELLO WORLD' is encrypted by atbash to 'HELLO WORLD'")
else:
    print("WRONG: 'HELLO WORLD' is encrypted by atbash to 'HELLO WORLD' but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")
