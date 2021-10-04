# from the course: "first steps in computering and python", 6.8.2

# Way One

def xor_cipher(msg, key):
    # delete pass and fill in your code below
    res = ""
    for i in range(0,len(msg)):
        if (msg[i] == "0"and key[i] == "0") or (msg[i] == "1"and key[i] == "1"):
            res += "0"
        elif (msg[i] == "0"and key[i] == "1") or (msg[i] == "1"and key[i] == "0"):
            res += "1"
    return res

# Way Two:
def xor_cipher(msg, key):
    # delete pass and fill in your code below
    res = ""
    for i in range(0,len(msg)):
        evenbit = int(key[i]) - int(msg[i])
        res += str(evenbit)
    return res

# Way three
def xor_cipher(msg,key):
    res = ""
    for i in range(0,len(msg)):
        if msg[i] == key [i]:
            res = res + "0"
        else:
            res = res + "1"
    return res

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Encrypting '00000' with '11111'")
ans = xor_cipher('00000', '11111')
if ans == '11111':
    print("CORRECT: Encypting '00000' with '11111' is '11111'")
else:
    print("WRONG: Encypting '00000' with '11111' is '11111' but the code returned", ans)

print("********************")
print("Encrypting '10101' with '10101'")
ans = xor_cipher('10101', '10101')
if ans == '00000':
    print("CORRECT: Encypting '10101' with '10101' is '00000'")
else:
    print("WRONG: Encypting '10101' with '10101' is '00000' but the code returned", ans)

print("********************")
print("Encrypting '10101110101010110101' with '00101011101010101010'")
ans = xor_cipher('10101110101010110101', '00101011101010101010')
if ans == '10000101000000011111':
    print("CORRECT: Encypting '10101110101010110101' with '00101011101010101010' is '10000101000000011111'")
else:
    print(
        "WRONG: Encypting '10101110101010110101' with '00101011101010101010' is '10000101000000011111' but the code returned",
        ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")
