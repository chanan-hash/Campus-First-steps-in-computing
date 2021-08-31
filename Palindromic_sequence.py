# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/63dbd8dc1b024cc38287684346c01769/cb84b5c56bb1435c88c4e061ceae1b58/

# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/63dbd8dc1b024cc38287684346c01769/22c5c1fceea8469d88cdc52bb055ae05/?child=first

def is_palindrome(st):
    # delete pass and fill in your code below
    l = 0
    r = len(st) - 1
    while l < r:
        if st[l] != st[r]:
            return False
        else:
            l = + 1
            r -= 1
        return True

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking if 'anna' is a perfect palindrome")
ans = is_palindrome('anna')
if ans == True:
    print("CORRECT: 'anna' is a perfect palindrome")
else:
    print("WRONG: 'anna' is a perfect palindrome but the code returned", ans)

print("********************")
print("Checking if 'A man, a plan, a canal, Panama' is a perfect palindrome")
ans = is_palindrome('A man, a plan, a canal, Panama')
if ans == False:
    print("CORRECT: 'A man, a plan, a canal, Panama' is not a perfect palindrome")
else:
    print("WRONG: 'A man, a plan, a canal, Panama' is not a perfect palindrome but the code returned", ans)

print("********************")
print("Checking if 'a nN.a' is a perfect palindrome")
ans = is_palindrome('a nN.a')
if ans == False:
    print("CORRECT: 'a nN.a' is not a perfect palindrome")
else:
    print("WRONG: 'a nN.a' is not a perfect palindrome but the code returned", ans)

### EXTRA TESTS ###

### DO NOT MODIFY, THIS PART OF THE CODE CHECKS THAT ###
### YOU HAVE UESD range ACCORDING TO INSTRUCTIONS ###
print(is_palindrome('radar radar'))
# True
print(is_palindrome('Anna'))
# False


print()
# second practice
# not a perfect palindrome

def is_general_palindrome(st):
    # delete pass and fill in your code below
    st = st.lower()
    st = st.replace(" ", "")
    st = st.replace(",", "")
    st = st.replace(".", "")

    return is_palindrome(st)


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking if 'anna' is a general palindrome")
ans = is_general_palindrome('anna')
if ans == True:
    print("CORRECT: 'anna' is a general palindrome")
else:
    print("WRONG: 'anna' is a general palindrome but the code returned", ans)

print("********************")
print("Checking if 'A man, a plan, a canal, Panama' is a general palindrome")
ans = is_general_palindrome('A man, a plan, a canal, Panama')
if ans == True:
    print("CORRECT: 'A man, a plan, a canal, Panama' is a general palindrome")
else:
    print("WRONG: 'A man, a plan, a canal, Panama' is a general palindrome but the code returned", ans)

print("********************")
print("Checking if 'a nN.a' is a general palindrome")
ans = is_general_palindrome('a nN.a')
if ans == True:
    print("CORRECT: 'a nN.a' is a general palindrome")
else:
    print("WRONG: 'a nN.a' is a general palindrome but the code returned", ans)

print("********************")
print("Checking if 'radat' is a general palindrome")
ans = is_general_palindrome('radat')
if ans == False:
    print("CORRECT: 'radat' is not a general palindrome")
else:
    print("WRONG: 'radat' is not a general palindrome but the code returned", ans)

print(is_general_palindrome('A man, a plan, a canal, Panama'))
#True
print(is_general_palindrome('Anna'))
#True
print(is_general_palindrome('anna'))
#True
print(is_general_palindrome('radxr'))
# False

### EXTRA TESTS ###

### DO NOT MODIFY, THIS PART OF THE CODE CHECKS THAT ###
### YOU HAVE UESD range ACCORDING TO INSTRUCTIONS ###

#import validation

print("********************")
print("\n\nNow checking your implementation:")

print("Checking that is_general_palindrome calls is_palindrome")
#if validation.test_general_calls_perfect(is_general_palindrome):
#    print("CORRECT: Very good, is_general_palindrome calls is_palindrome")
#else:
#    print("WRONG: is_general_palindrome does not call is_palindrome")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")