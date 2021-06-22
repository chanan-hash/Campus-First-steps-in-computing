str = "hello, world!"
COMMA = ", "
print(str.split(COMMA)[0])
# split without anything creates list with the word themself of the string
# if we put a index we will get the word itself no in a list - very important to notice
# because this is a difference between string and list format, we are asking/getting the objectqword inside the index itself
# when split getting an object inside it it split the string acorrding to the object

str11 = "Hello, my name is Chanan"
print(str11.split())
# ['Hello,', 'my', 'name', 'is', 'Chanan']
print(str11.split()[2])
# name
print(str11.split(COMMA))
# ['Hello', 'my name is Chanan']
print(str11.split(COMMA)[1])
# my name is Chanan

str12 = "Hi, how are you? isn't that a lovely day?"
# lets put now bunch of commas to see how it will split it
str13 = "Hi, how are you, isn't that, a lovely day?"
print(str13.split(COMMA))
# ['Hi', 'how are you', "isn't that", 'a lovely day?']
# Every object in the list is acorrding to were is the comma (",")

# remove and replace
str14 = "hello every one, how are you"
# it replace all the places with the first char with the second
print(str14.replace("e","a"))
# if we want to remove a char, we can replace it with empty string("")
print(str14.replace("e",""))
# if we put a number it replace the char the as much as the number we have put
print(str14.replace("e","",1))
# here it will replace "e" with "a" only once

print()
# join
str15 = "WOW!! that was amazing!"
print(str15.join(["!","abc"]))
# join on string need to get a list with string, and it adds it after the given string
print(".".join(["abc","def","ghi"]))


print()

#  From the course "First steps in computing and python"
# middle test questions 5-6

# A func' to check if a string has the to same characters one near each other like
# "abcc" - True
# "abcb - False, because "b" is not near the second "b"

# The psa code:
'''
הגדרת הבעיה: האם יש במחרוזת שני תווין רוצפים זהים (קלט - מחרוזת st, באורך n)
לכל אינדקס בין 1 ל n-1 (כולל) .1
    אם התו באינדקס i שווה לתו באינדקס i-1:
        החזר True
החזר False

פונקציה תמיד מחזירה פקודת return אחת (שיוכלה לכלול כמה דברים), לכן לא צריך else

# אם נשתמש ב i+1, נגיע לערך אינדקס שמחוץ לרשימה, לכן זה תמיד האיבר הראשון והאיבר הקודם לו
זה למה אנחנו מתחילים לספור מ 1, ולא מ 0, כי האיבר הקודם ל 0 הוא 1- ואין אינדקס כזה
צריך לשים לב שמיקומים באינדקס יהיו מאוזנים ונכונים ובטווח המתאים וטווח קיים
גם בתחילת הרשימה וגם בסופה

# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/88597be83ed643e6b980a785e81a75de/ae43e355bf4640a5afb076278106f56d/?child=first
'''
def twice(st):
    # delete pass and fill in your code below
    for i in range(1, len(st)):
        if st[i] == st[i - 1]:
            return True
    return False


### TESTS ###
print(twice("abcc"))
print(twice("abcb"))
print("********************")
print("Starting the test:")

print("********************")
print("Checking if 'abcdefgabcdefg' has two consecutive similar chars")
ans = twice('abcdefgabcdefg')
if ans == False:
    print("CORRECT: 'abcdefgabcdefg' has no consecutive similar chars")
else:
    print("WRONG: 'abcdefgabcdefg' has no consecutive similar chars but your code returned", ans)

print("********************")
print("Checking if 'aabbccddeeffgg' has two consecutive similar chars")
ans = twice('aabbccddeeffgg')
if ans == True:
    print("CORRECT: 'aabbccddeeffgg' has consecutive similar chars")
else:
    print("WRONG: 'aabbccddeeffgg' has consecutive similar chars but your code returned", ans)

print("********************")
print("Checking if 'abcdd' has two consecutive similar chars")
ans = twice('abcdd')
if ans == True:
    print("CORRECT: 'abcdd' has consecutive similar chars")
else:
    print("WRONG: 'abcdd' has consecutive similar chars but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()

# count Func' - counting how namy times is a given char in a string
str16 = "abcdskrwkwalvkaakvls"
print(str16.count("a"))

print()

# slicing Func'

str17 = "abcdefg"
print(slice(str17[1:4]))
print(str17[0:3])
