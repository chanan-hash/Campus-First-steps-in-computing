# Final Test code board answers
# From the course "First steps in computing and python"
# Question number 6

def has_sum(L, k):
    # delete pass and fill in your code below
    for i in L:
        for j in L:
            if i + j == k and i in L and j in L:
                return True
    return False


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking if [3, 5, -7, 20, -1] has two elements that sum to 8")
ans = has_sum([3, 5, -7, 20, -1], 8)
if ans == True:
    print("CORRECT: 3 + 5 = 8 and 3, 5 are in [3, 5, -7, 20, -1]")
else:
    print("WRONG: 3 + 5 = 8 and 3, 5 are in [3, 5, -7, 20, -1] but your code returned", ans)

print("********************")
print("Checking if [3, 5, -7, 20, -1] has two elements that sum to -8")
ans = has_sum([3, 5, -7, 20, -1], -8)
if ans == True:
    print("CORRECT: -7 + -1 = -8 and -7, -1 are in [3, 5, -7, 20, -1]")
else:
    print("WRONG: -7 + -1 = -8 and -7, -1 are in [3, 5, -7, 20, -1] but your code returned", ans)

print("********************")
print("Checking if [1, 2, 4, 8] has two elements that sum to 17")
ans = has_sum([1, 2, 4, 8], 17)
if ans == False:
    print("CORRECT: [1, 2, 4, 8] has no pair of elements that sum to 17")
else:
    print("WRONG: [1, 2, 4, 8] has no pair of elements that sum to 17 but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

res1 = has_sum([1,2,3], 5)  # 2+3
res2 = has_sum([1,2,3], 6)  # 3+3
res3 = has_sum([1,1,1], 2)  # 1+1
res4 = has_sum([1,2,3], 1)

print(res1, res2, res3, res4)
# answer = True True True False

print()
# Question number 8

def count_above(L, grade):
    # delete pass and fill in your code below
    count = 0
    for i in L:
        if i >= grade:
            count += 1
    return count


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking with L = [100, 100, 100, 100], grade = 60")
ans = count_above([100, 100, 100, 100], 60)
if ans == 4:
    print("CORRECT: All grades in [100, 100, 100, 100] are at least 60")
else:
    print("WRONG: All grades in [100, 100, 100, 100] are at least 60 but your code returned", ans)

print("********************")
print("Checking with L = [60, 70, 80, 90, 100], grade = 70")
ans = count_above([60, 70, 80, 90, 100], 70)
if ans == 4:
    print("CORRECT: Four grades in [60, 70, 80, 90, 100] are at least 70")
else:
    print("WRONG: Four grades in [60, 70, 80, 90, 100] are at least 70 but your code returned", ans)

print("********************")
print("Checking with L = [60, 70, 80, 90], grade = 100")
ans = count_above([60, 70, 80, 90], 100)
if ans == 0:
    print("CORRECT: No grades in [60, 70, 80, 90] are at least 100")
else:
    print("WRONG: No grades in [60, 70, 80, 90] are at least 100 but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()

# Question number 9

def max2(a,b):
    if a>b:
        return a
    else:
        return b

def max4(a1, a2, a3, a4):
    ## Fix the code below, your code must call the function max2!
    return max2(max2(a1,a2), max2(a3,a4))


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking maximum in 1, 2, 3, 4 using max4")
ans = max4(1, 2, 3, 4)
if ans == 4:
    print("CORRECT: Very good, max4 returned 4")
else:
    print("WRONG: the maximal number is 4 but max4 returned", ans)

print("********************")
print("Checking maximum in 4, 4, 4, 4 using max4")
ans = max4(4, 4, 4, 4)
if ans == 4:
    print("CORRECT: Very good, max4 returned 4")
else:
    print("WRONG: the maximal number is 4 but max4 returned", ans)

print("********************")
print("Checking maximum in 4, 3, 2, 1 using max4")
ans = max4(4, 3, 2, 1)
if ans == 4:
    print("CORRECT: Very good, max4 returned 4")
else:
    print("WRONG: the maximal number is 4 but max4 returned", ans)

### EXTRA TESTS ###

### DO NOT MODIFY, THIS PART OF THE CODE CHECKS THAT ###
### YOU HAVE CALLED max2 AND max3 ACCORDING TO INSTRUCTIONS ###

print("********************")
print("\n\nNow checking your implementation:")

import inspect
import ast

def test_max2(f):
    call_names = [c.func.id for c in ast.walk(ast.parse(inspect.getsource(f)))
          if hasattr(c,'func') and hasattr(c.func,'id') and isinstance(c, ast.Call)]
    return ("max2" in call_names)

print("********************")
print("Checking that max4 calls max2")
if test_max2(max4):
    print("CORRECT: Very good, max4 calls max2")
else:
    print("WRONG: max4 does not call max2")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()

# Question number 10
def binary_search(my_list, x):
    left = 0
    right = len(my_list) - 1

    while left <= right:
        mid = (left + right) // 2
        # print(mid, my_list[mid])
        print(my_list[mid])
        if my_list[mid] == x:
            return True
        else:
            if my_list[mid] < x:  # go to right half
                left = mid + 1
            else:  # go to left half
                right = mid - 1
    return False  # if we got here the search failed

binary_search([100,110,120,130,140,150,160,170],135)

print()

# Question number
n = 2000
while n > 0:
    print(n)
    n = n // 2

def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)

    return sorted_L

lst = [1,2,3,4,5,6,7,8,9,0]
print(selection_sort(lst))

print()
# Question number 15 - encryption & decryption
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
cipher = "fbyyg ugxym ap l paihyb hxgoxli"

x = sub_decrypt(cipher, alphabet, shuffled)
print(x)
y = caesar_break(x)
print(y) # look at offset 14

print()


# Question number 16
def add(im, k):
    w, h = im.size
    im_new = im.copy()
    mat_new = im_new.load()

    for x in range(w):
        for y in range(h):
            mat_new[x, y] = (mat_new[x, y] + k)%256

    return im_new

# add(img,256).show()

print()

# Question number 18, creating a grey triangle
### DO NOT MODIFY THIS CODE ###
### THIS CODE LETS YOU VIEW THE IMAGE YOU MAKE ###
### USING im.show() ###

from PIL import Image
import urllib
import random


def display_image(im):
    fn = str(random.randint(1, 500)) + ".bmp"
    im.save(fn)
    print("<img src=\"/resources/{}\">".format(fn))
    print("")


Image.Image.show = display_image


### YOU CAN MODIFY BELOW THIS LINE ###

def triangle(n):
    # delete pass and fill in your code below
    img = Image.new('L', (n, n), 255)
    mat = img.load()
    for x in range(n):
        for y in range(n):
            if x >= y:         # --> this is the line that making the triangle
                mat[x, y] = 128
    return img


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking for n = 4")
ans = triangle(4)
test = [128, 128, 128, 128, 255, 128, 128, 128, 255, 255, 128, 128, 255, 255, 255, 128]
if type(ans) == Image.Image and list(ans.getdata()) == test:
    print("CORRECT: A proper triangle was drawn for n = 4")
else:
    print("WRONG: An improper triangle was drawn for n = 4")

print("********************")
print("Checking for n = 5")
ans = triangle(5)
test = [128, 128, 128, 128, 128, 255, 128, 128, 128, 128, 255, 255, 128, 128, 128, 255, 255, 255, 128, 128, 255, 255,
        255, 255, 128]
if type(ans) == Image.Image and list(ans.getdata()) == test:
    print("CORRECT: A proper triangle was drawn for n = 5")
else:
    print("WRONG: An improper triangle was drawn for n = 5")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")