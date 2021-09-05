# From the course "First steps in computing and python"
# 5.4.2
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/36e348653c954c5994d70d4171ab9321/?child=first

# This code is under the subject of fixing bit errors

# to understand idea look it on the link above
# here we will just have the Functions

# Do not change the existing code, only fill in line 6 after result =
def repeat3(msg):
    result = ""
    for bit in msg:
        # result = result + (bit * 3)
        # in a string if we multiple it, it repeat the string the times we multiple it - "a" * 3 = "aaa"
        result += bit * 3
        # if we want to see in every iteration the repeated bit
    #    print(result)
    return result

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Encoding '100'")
ans = repeat3('100')
if ans == '111000000':
    print("CORRECT: '100' is encoded by '111000000'")
else:
    print("WRONG: '100' is encoded by '111000000' but your code returned", ans)

print("********************")
print("Encoding '1'")
ans = repeat3('1')
if ans == '111':
    print("CORRECT: '1' is encoded by '111'")
else:
    print("WRONG: '1' is encoded by '111' but your code returned", ans)

print("********************")
print("Encoding '001'")
ans = repeat3('001')
if ans == '000000111':
    print("CORRECT: '001' is encoded by '000000111'")
else:
    print("WRONG: '001' is encoded by '000000111' but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

# if we want to chose the times it will repeat it self:
def repeat(msg,k):
    result = ""
    for bit in msg:
        result += bit * k
        # if we want to see in every iteration the repeated bit
    #    print(result)
    return result

# Modify the code as follows:
#   Change the function name to repeat
#   Add a second input variable k after msg
#   Each bit should be copied k times instead of 3 times

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Encoding '100' with k = 3")
ans = repeat('100', 3)
if ans == '111000000':
    print("CORRECT: '100' is encoded by '111000000'")
else:
    print("WRONG: '100' is encoded by '111000000' but the code returned", ans)

print("********************")
print("Encoding '1' with k = 5")
ans = repeat('1', 5)
if ans == '11111':
    print("CORRECT: '1' is encoded by '11111'")
else:
    print("WRONG: '1' is encoded by '11111' but the code returned", ans)

print("********************")
print("Encoding '001' with k = 7")
ans = repeat('001', 7)
if ans == '000000000000001111111':
    print("CORRECT: '001' is encoded by '000000000000001111111'")
else:
    print("WRONG: '001' is encoded by '000000000000001111111' but the code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

### restore ###

def restore3(bits):
    result = ""
    for i in range(0, len(bits), 3):
        triplet = bits[i] + bits[i+1] + bits[i+2]
        if triplet.count("0") >= 2:   # 2 or 3 zeros
            result = result + "0"
        else:
            result = result + "1"
    return result

bits = "000111111"
print(restore3(bits))

# if we want to chose the times it will repeat it self:
# we can make a global variable that will be the same for the repeating and the restoring, so it eill be suitable and not differet in each part
# if it will bw different in each part it can cause problems in the translation of the 'bits'.
# but for the idea we will give the example

def restore3_2(bits,a):
    result = ""
    for i in range(0, len(bits), a):
        triplet = bits[i] + bits[i+1] + bits[i+2] #.....bits[i+n] here it suppose to be till "i+n"
    # count inbuilt Func' is counting how many times we have the given char in a string
        if triplet.count("0") >= 2:   # 2 or 3 zeros, so actually it is - triplet.count("0") >= n//2 + 1
            result = result + "0"
        else:
            result = result + "1"
    return result

# making this code "generalization" in the actuaaly restore part -----     triplet = bits[i] + bits[i+1] + bits[i+2]....
# to see how to make the restore Func' "generalization" read in the end of the page in the link below:
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/36e348653c954c5994d70d4171ab9321/?child=first

# we need a loop which doing k iterations using something called in python --- "slicing"

# Now we will do 'restore' Func' in a generalization way:
# we used the second wat with slicing operation and not with nested loop
def restore(msg, k):
    # delete pass and fill in your code below
    result = ""
    for i in range(0, len(msg), k):
        k_bits = msg[i:i + k]
        if k_bits.count("0") > k_bits.count("1"):  # we have 0 more times than 1
            result = result + "0"
        else:
            result = result + "1"
    return result

# By the first wat with nested loops
# for more understanding look in the link:
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/36e348653c954c5994d70d4171ab9321/?child=first
def restore_2(msg, k):
    result = ""
    for i in range(0, len(msg), k):
        k_bits = ""
        for j in range (i,i+k):
            k_bits += msg[j]
        if k_bits.count("0") > k_bits.count("1"):   #we have 0 more times than 1
            result = result + "0"
        else:
            result = result + "1"
    return result

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Decoding '1111100000' with k = 5")
ans = restore('1111100000', 5)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Decoding '0111101010' with k = 5")
ans = restore('0111100110', 5)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Decoding '11110000101010' with k = 7")
ans = restore('11110000101010', 7)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()

############## THIS IS 5.4.5 ########
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/36e348653c954c5994d70d4171ab9321/?child=first

# this code is if the transmit was a only one 'bit'
# using ouer counting variable
def restore_single(single_msg):
    # We initialize counters
    cnt1 = 0
    cnt0 = 0

    # We go over the characters in the message
    for bit in single_msg:
        if bit == "1":
            cnt1 = cnt1 + 1
        else:
            cnt0 = cnt0 + 1

    if cnt1 > cnt0:
        return "1"
    else:
        return "0"

print(restore_single("1111111"))
print(restore_single("0101010"))
print(restore_single("100000000000001"))

print()

# 5.4.5
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/36e348653c954c5994d70d4171ab9321/?child=first

# here we dividing the string in part according to k. we starting for a given index (i) till the index plus k.
def get_block(msg, i, k):
    # We initialize an empty string
    k_bits = ""

    # We go over the characters in the appropriate indices
    for j in range(i, i + k):
        k_bits = k_bits + msg[j]

        # usnig slicing operation
       # block = msg[i:i + k]

    # We return the result
    return k_bits
    # return block

print(get_block("100010100111010110010", 6, 3))
print(get_block("11100", 0, 5))

print()
######## The final code for the problem of "bit massage" ##########

# The complete solution

def restore(msg, k):
    # We initialize an empty string
    result = ""
    # We got over the message in k-bit blocks
    # the answer for level 2 in the first psa-code, how to go over the string "msg" in k length jumps. the string must be a k times something, because we multiple it with k.
    # se more in the web site there is a link upwards somewhere - 5.4.5
    for i in range(0, len(msg), k):
        # We get the next block
        k_bits = get_block(msg, i, k)

        # We restore it
        bit = restore_single(k_bits)

        # We add the bit to our result
        result = result + bit
    return result

def get_block(msg, i, k):
    # We initialize an empty string
    k_bits = ""

    # We go over the characters in the appropriate indices
    for j in range(i, i + k):
        k_bits = k_bits + msg[j]

    # We return the result
    return k_bits

def restore_single(single_msg):
    # We initialize counters
    cnt1 = 0
    cnt0 = 0

    # We go over the characters in the message
    for bit in single_msg:
        if bit == "1":
            cnt1 = cnt1 + 1
        else:
            cnt0 = cnt0 + 1

    if cnt1 > cnt0:
        return "1"
    else:
        return "0"

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Decoding '1111100000' with k = 5")
ans = restore('1111100000', 5)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Decoding '0111101010' with k = 5")
ans = restore('0111100110', 5)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print("********************")
print("Decoding '11110000101010' with k = 7")
ans = restore('11110000101010', 7)
if ans == '10':
    print("CORRECT: The original message was '10'")
else:
    print("WRONG: The original message was '10' but the code returned", ans)

print()

### answer for question 8 in the test for lesson 5 ###

def parity(msg):
    # delete pass and fill in your code below
    for i in msg:
        if msg.count("1") % 2 == 0:
            return True
        else:
            return False

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking if '101' is a valid string")
ans = parity('101')
if ans == True:
    print("CORRECT: '101' is a valid encoding")
else:
    print("WRONG: '101' is a valid encoding but your code returned", ans)

print("********************")
print("Checking if '11000' is a valid string")
ans = parity('11000')
if ans == True:
    print("CORRECT: '11000' is a valid encoding")
else:
    print("WRONG: '11000' is a valid encoding but your code returned", ans)

print("********************")
print("Checking if '1011' is a valid string")
ans = parity('1011')
if ans == False:
    print("CORRECT: '1011' is NOT a valid encoding")
else:
    print("WRONG: '1011' is a NOT a valid encoding but your code returned", ans)

print("********************")
print("Checking if '000000' is a valid string")
ans = parity('000000')
if ans == True:
    print("CORRECT: '000000' is a valid encoding")
else:
    print("WRONG: '000000' is a valid encoding but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()
# answer for question 9 in the test for lesson 5

def rep_and_parity(msg):
    # delete pass and fill in your code below
    result = ""
    for bit in msg:
        result += bit * 3

    par = 0
    for chr in result:
        if chr == "1":
            # counting jow mant times we have 1, in the stirng
            par = par + 1

    # parity check
    # it is even
    if par % 2 == 0:
        result += "0"
    # it is odd
    else:
        result += "1"

    return result

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Encoding '101'")
ans = rep_and_parity('101')
if ans == '1110001110':
    print("CORRECT: '101' is encoded as '1110001110'")
else:
    print("WRONG: '101' is encoded as '1110001110' but your code returned", ans)

print("********************")
print("Encoding '100'")
ans = rep_and_parity('100')
if ans == '1110000001':
    print("CORRECT: '100' is encoded as '1110000001'")
else:
    print("WRONG: '100' is encoded as '1110000001' but your code returned", ans)

print("********************")
print("Encoding '111'")
ans = rep_and_parity('111')
if ans == '1111111111':
    print("CORRECT: '111' is encoded as '1111111111'")
else:
    print("WRONG: '111' is encoded as '1111111111' but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")