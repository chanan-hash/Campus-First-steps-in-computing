# From the course "First steps in computing and python"
# 6.6.1/2

# The psa code is very similar to caesar cipher, with a little bit changes
# here is the link for it
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/e4908534f9904cd4b6ee0e51f1c99b21/8c9e5b5fd0134825bdc1cd9bf9ce00cc/?child=first

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

alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "psfvinytdugqrjhwebmkzoxcla"

print(sub_encrypt("hello world", alphabet, shuffled))
print(sub_encrypt("hello world!", alphabet, shuffled))

print()
# The decrypting is actually in the same way but is the oposite direction, a little bit like the decrypting in Caesar cipher. We are going backward and getting the original plaintext
print(sub_encrypt("tiqqh xhbqv",shuffled , alphabet)) # here we've taken the encrypt text, and we "encrypt" it again with the shuffeld alphabet, that it is for it as regular alphabet. and the shuffled one is the alphabet we know
# that is gvinig us the decrypt text, we did the wat back. but actually we encrypt the encrypt text.

print()
# 6.6.4 question
# trying to do Caesar cipher with sub encrypt when you have already know the offset, which in this case it is 5

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


def caesar_encrypt5(plaintext):
    # Write your solution here (don't forget to use sub_encrypt!):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = alphabet[position + 5] # We didn't used shuffeld 'alphabet'
            #  we used the same alphabet and added 5 to the position, which will be insted the offset. it will make a new "alphabet with another position
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")

    return ciphertext


print("********************")
print("Starting the test:")

print("********************")
print("Encrypting 'abcde'")
ans = caesar_encrypt5("abcde")
if ans == "fghij":
    print("CORRECT: 'fghij' is the correct encryption of 'abcde'")
else:
    print("WRONG: 'fghij' is the correct encryption of 'abcde',  but the code returned", ans)

print("********************")
print("Encrypting 'hello!'")
ans = caesar_encrypt5("hello!")
if ans == "mjqqt!":
    print("CORRECT: 'mjqqt!' is the correct encryption of 'hello!'")
else:
    print("WRONG: 'mjqqt!' is the correct encryption of 'hello!',  but the code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()
# 6.6.5 question
# if we want to add an offset to sub encrypt and like that it will be as a caesar cipher.
# we are taking the Func' we used in the last qustion, but insted adding 5n we will add to the position a givven offset

# actually caesar cipher is a privet case of subsitution encrypt (when the shuffeld alphabet in known and not randomly)
def caesar_encrypt_new(plaintext, offset):
    # Write your solution here (don't forget to use sub_encrypt!):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = alphabet[position + offset]
            # print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            # print(char, "unchanged")

    return ciphertext


print("********************")
print("Starting the test:")

print("********************")
print("Encrypting 'abcde' with offset=1")
ans = caesar_encrypt_new("abcde", 1)
if ans == "bcdef":
    print("CORRECT: 'bcdef' is the correct encryption of 'abcde'")
else:
    print("WRONG: 'bcdef' is the correct encryption of 'abcde',  but the code returned", ans)

print("********************")
print("Encrypting 'hello!' with offset=10")
ans = caesar_encrypt_new("hello!", 10)
if ans == "rovvy!":
    print("CORRECT: 'rovvy!' is the correct encryption of 'hello!'")
else:
    print("WRONG: 'rovvy!' is the correct encryption of 'hello!',  but the code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()

# 6.6.6 Subsitution decrypt!!!
# Like caesar cipher decrypt, here to decrypt we've just went the way back of the encrypt
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

# we are actually ecrypting the encrypted text, but now the shuffeld is the alphabet, which make it like we decrypt the cipher text
def sub_decrypt(ciphertext, alphabet, shuffled):
    plaintext = sub_encrypt(ciphertext, shuffled, alphabet)
    return plaintext

alphabet = "abcdefghijklmnopqrstuvwxyz"
shuffled = "iczsflxpoyguvhrmjewadtnqbk"

ciphertext = sub_encrypt("hello world", alphabet, shuffled)
print(ciphertext)
plaintext = sub_decrypt(ciphertext,alphabet,shuffled) # in the Func' itself is swiching betweeen  alphabet and shuffled
print(plaintext)

print()
# 6.6.8
# How to create your own shuffled alphabet
# we will use the random package and function "shuffle"
import random
L = [1,2,3,4,5]
random.shuffle(L)
print(L)
print()
# The problem that, the Func' "shuffle" needs to get a list and not a string to work
# fpr that we will take a string, convert it to a list of characters, and then activate the "shuffle" Func' and make it shuffled
# Then we will convert the list back to a string

# Try running the code multiple times. Each execution will give a different re-ordering of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet)
L = list(alphabet)   # convert str to list, by the Func' "list"
print(L)
random.shuffle(L)
shuffled = "".join(L)   # convert list to str, it is taking empty string, and "join" it the characters from the list
print(shuffled)

print()
# Breaking Sub_encrypt
# what that we will do, we'll see the frequency of the letter, and like that we can try and see if we are getting we a logical sentence

# Function for the frequency/rarity of the letter in a given text
def char_count(text):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        how_many = text.count(char)
        if how_many > 0: # a condition that we won't need to print each letter
            percent = how_many * 100 / len(text)
            print(char, "frequency:", percent, "%")

char_count("aaab")
char_count("Subsitiution")
print()

# if we want to find only the second frequent lettern and don't want the Func' to print and calculate all the letter it can takes some time/
# First we will find the letter which is the most frequnet, with the maximun number
# the we will find the maximum letter that is but it is not the max' we had befor - the second max'

# to find the first max' letter we will use this psa-code

def frequent_char(text):
    # Initialize temp variables
    temp_char = ""
    maximum = 0

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Go over each char in the alphabet
    for char in alphabet:
        cnt = text.count(char)

        # Check if it is most frequent so far
        if cnt > maximum:
            maximum = cnt
            temp_char = char

    return temp_char

# now after we have a function for finding the most frequent letter in a text we will use it to findd the secont frequent letter
# it will work the same, but here we will also check if the max letter is different from the most frequent letter we've found
def second_frequent(text):
    # Initialize temp variables
    temp_char = ""
    maximum = 0

    # Find most frequent char, by using the function we've made
    max_char = frequent_char(text)

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Go over each char in the alphabet
    for char in alphabet:
        cnt = text.count(char)

        # Check if it is most frequent so far apart from maximal char
        if cnt > maximum and char != max_char:
            maximum = cnt
            temp_char = char

    return temp_char

english = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30]Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation."
print(frequent_char(english))
print(second_frequent(english))

# another way of doing the function for finding the second frequnet letter
print()
# For finding a frequency of a given number 'k', and not only the first or secind one, see in the link below in the end of the page
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/e4908534f9904cd4b6ee0e51f1c99b21/6b2dfb90a4e04c05af094fec43a4c237/?child=first
# The basic tool we are using is not the idea of finding the max times letter apears, but rather using sort concep

# trying to make char_count with less complexity
def char_count(text):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        how_many = text.count(char)
        if how_many > 0:
            percent = how_many * 100 / len(text)
            print(char, "frequency:", percent, "%")

def char_count_better(text):
    # Write your solution here:
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for char in text:
        if char in alphabet and char not in new_string:
            new_string = new_string + char
            how_many = new_string.count(char)
            percent = how_many * 100 / len(text)
            print(char, "frequency:", percent, "%")

# DO NOT CHANGE
from urllib.request import urlopen
alice = str(urlopen("https://www.gutenberg.org/files/11/11-0.txt").read())

# WRITE YOUR TESTS HERE:
char_count(alice)
char_count_better(alice)