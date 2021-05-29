def intersection(list1, list2):
    return set(x==y for x in list1 for y in list2)
print(intersection([1,2,3],[3,4,5]))


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# long way for mission 1.3.1
def intersection1(a,b):
    c = []
    for x in a:
        for y in b:
            if x==y:
                c.append(x)
    return set(c)
#              return x
 #           else:
#                continue

print(intersection1([1,2,3,4],[3,4,5]))


name = "Chanan"
age = 22.5

print(f"My name is {name} and I am {age} years old")

# short way for mission 1.3.1
l1 = [1,2,3,4]
l2 = [8,3,9]

def inter_l(list1,list2):
    return [x==y for x in list1 for y in list2]
print(inter_l(l1,l2))

op = set(l1+l2)
print(op)



#mission 1.3.2

def is_prime(n):
    if_prime = ["Prime" if x%x == 0 and x%1 == 0  else "Not Prime" for x in n]
    return  if_prime
#print(is_prime(5))

def is_prime_v2(number):
    if number%number ==0 and number%1==0:
        print("Prime")
    else:
        print("Not Prime")
# it is not so correct because it ca stil be divided in more number like four


def is_prime_v3(x):
# prime_list = [x for x in range(10, 11) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
    return [x for x in range(10, 11) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
#print(is_prime_v3(4))
print()
#mission 1.3.3
def is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True

# make it in one liner
string = "hahahahahaha"
#is_funny1 = [for char in string if char !="a" if char !="h"]

# we can put it in a function
print()
#mission 1.3.4
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

def caesar_code(s):
## נמיר אתר התו למספר נוסיף לו 2, על מנת שנוכל להזיז את התו שני צעדים קדימה,
# ואחר מכן נמיר בחזרה את המספר החדש לתו בחזרה. שהוא בעצם התו/האות שנמצא שני צעדים קדימה
    st = ""
    for i in s:
        i = s.replace(i,chr(ord(i)+2))
        # לשרשר למרוזת החדשה את התו המוחלף
    st += i
    return st
    #lst = []
    #s = s.split()
    #s = s.split()
    #for i in s:
     #  s[i] = s.replace(chr(ord(s) + 2))
     #  lst.append(i)

        # במקם append להתשתמש ב join

    #return str(lst)

print(caesar_code(password))

def caesar_cipher(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

    # from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
    #from  https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
print(caesar_cipher(password,2))

# in one line:
print(["".join(chr(ord(ch) + 2) for ch in password.lower()) for word in password ])
# from https://stackoverflow.com/questions/28652984/caesar-shift-on-list-elements-using-list-comprehension
print()

def caesar_cipher2():
    print("The decrypted text is: "+"".join(map(lambda x: chr(ord(x)+y),x)))

# הסבר לרעיון של הדבר

# ע"י map אני אומר שאני רוצה להפעיל על כל הרשימה (או שניים) פעולה מסויימת
# הפעולה הזאת תהיה פעולה קצרה ע"י למבדה
# הפעולה תקבל תו, תמיר אותו למספר ע"י ord תוסיף לו שניים, על מנת שנקדם אותו קדימה בצורה המספרית שלו (ASCII) עיין בנושא הזה
# בקורס צעדים ראשונים במדעי המחשב ותכנות מסבירים על הנושא הזה, בגדול לכל תו ואות יש ייצוג מספרי שאותו אחרי זה ניתן להמיר לשפה בינארית ובכך וקבל בעצם אות שמומרת לשפה בינארית
# אחרי זה ממירים אותו בחזרה לתו ע"י chr שממיר מספר לאות
# ואותו ע"י join אנחנו משרשרים לרשימה ריקה שעשינו
# ואת כל זה מפעילילם על x מסוים שהוא הפרמטר (לא הפעולה) ש map צריכה לקבל (היא צריכה לקבל פרמטר/רשימה, ופעולה שהיא תפעל עליהם כזכור

def caesar_cipher3():
    print("The decrypted text is: "+"".join(map(lambda x=input("text: "),y=eval(input("shift: ")): chr(ord(x)+y),x)))

# from https://www.daniweb.com/programming/software-development/threads/358040/one-line-caesar-cipher-help
#caesar_cipher3()

print()
#קורס צעדים ראשונים במדעי המחשב ותכנות בפייתון, שיעור 2 בוחן שאלה 10.
# לקח לי זמן לשבת על הפונקציה הזאת אבל ב"ה פתרתי את זה אחרי כמה נסיונות
def mult_and_replace(string):
    # delete pass and fill in your code below
    x = str.count(string,"!")

    y = str.replace(string,"!","?")*x
    if "!" in string == False:
        return ""
    return y

ans = mult_and_replace("Sh!al!om!")
if ans == 'Sh?al?om?Sh?al?om?Sh?al?om?':
    print("CORRECT: Very good, Sh!al!om! was changed to Sh?al?om?Sh?al?om?Sh?al?om?")
else:
    print("WRONG: Sh!al!om! should change to Sh?al?om?Sh?al?om?Sh?al?om? but the code returned", ans)


print()

# The coin challange

def combine_coins1(coin, numbers): return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))

print(combine_coins1("$",range(5)))

# another answer with only list comprehension
def combine_coins2(coin, numbers):    return ', '.join([coin + str(i) for i in numbers])
print(combine_coins2("$",[1,2,3,4,5]))

#נסו לעקוב אחר הפתרונות ולהבינם.
# ודאי שמתם לב כי בכל אחד מן הפתרונות שורת הקוד ארוכה, עמוסה ולכן לא במיוחד קריאה.
# זכרו שבכתיבת קוד חשוב מאוד לשים לב למאפיינים שונים של הקוד, ביניהם מידת הקריאות שלו.
# לכן לעיתים נעדיף קוד ארוך וברור על פני קוד קצר וארור.

print()
import random;p = lambda:random.choice('7♪♫♣♠♦♥◄☼☽');[print('|'.join([p(),p(),p()]),end='\r') for i in range(8 ** 5)]

#שרות הקוד הזו, בעצם מגרילה שלושה תווים מהמחזורת הזו מצרפת אותם יחד עם רווח של | בטווח מסויים
# מתכנתים זכרו: לרוב נעדיף לכתוב קוד קריא על פני קוד קצר!
