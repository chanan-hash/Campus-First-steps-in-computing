#מתי נוכל לקבוע בוודאות שמצאנו פלינדרום?
# התהליך הזה יימשך כל עוד התו הימני שמשווים אכן נמצא מימין לתו השמאלי שמשווים.
# בפעם הראשונה שתנאי זה לא מתקיים, נוכל להכריז שהמחרוזת הנתונה היא אכן פלינדרום.
# שימו לב שלא צריך להמשיך לבצע את הבדיקה אחרי שמתקיים התנאי, כי ברגע שנעבור את האמצע נתחיל לבצע השוואות שכבר ביצענו קודם.
# רגע, אמרנו כל עוד?? אמרנו לולאת while!!
# הרבה פעמים הדרך שבה אנחנו מנסחים לעצמנו את האלגוריתם במילים מעידה על סוג הלולאה שאותה כדאי לבחור.
# במקרה הזה טבעי להשתמש בלולאות while, אם כי היה אפשר גם להשתמש בלולאות for.
# לפני שנקפוץ לממש את האלגוריתם הזה בפייתון, בואו נכתוב אותו בפסאודו קוד.
# נשתמש בשני משתנים שיכילו אינדקסים במחרוזת. הם יאותחלו לקצוות, ויזוזו פנימה בכל איטרציה.

#1. אתחל l=0, r=len(st)-1
#2. כל עוד l<r:
#2.1 אם st[l] לא שווה ל- st[r]:
#2.1.1 החזר False וסיים
#2.2 הגדל את l ב- 1 והקטן את r ב- 1
#3. החזר True

#בהתחלה נגדיר שני משתנים עם השמות l (left) ו-r (right).
# נאתחל את l לאינדקס השמאלי ביותר של המחרוזת, כלומר 0, ואת r לימני ביותר, כלומר אורך המחרוזת פחות 1 (פחות 1, כי מתחילים ב-0).
# ואז נריץ בלולאה כל עוד l<r, ונשווה את תווי המחרוזת באינדקסים l ו-r.
# אם הם שונים אנחנו יודעים בדיוק מה לעשות – לסיים את ריצת האלגוריתם ולהחזיר False.
# אם הם שווים, צריך להמשיך בלולאה, אבל לא לפני שנזיז את l מקום אחד ימינה, כלומר נגדיל אותו ב-1, ואת r נזיז שמאלה, כלומר נקטין אותו ב-1.
# משורה 2.2 חוזרים לבדוק את התנאי שבשורה 2 פעם נוספת.
# כך ממשיך התהליך עד שקורה אחד משניים:
# או שמתישהו מגלים תווים מתאימים ששונים זה מזה, ומחזירים False, או שהלולאה מסתיימת כי האינדקס l כבר לא קטן מהאינדקס r, כלומר או שהמשתנים l ו-r נפגשו,
# או שהם חלפו זה על פני זה.
# אחד מהשניים בטוח יקרה בשלב מוקדם או מאוחר.
# אם הלולאה הסתיימה מהסיבה השניה, אפשר סוף סוף להחזיר True.


# אנחנו עובדים ע"י תנאי שלילה, מה קורה אם לא. אנחנו לא מחפשים אם כן, אלא שזה יההי התנאי הבסיסי
# לפעמים קל יותר להגדיר תנאים בצד השולל מה קורה עם לא, מאשר לנסות להגדיר אותו בצד החיובי
# ראה על זה עוד פה בנושא "כמתים לוגים"
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/63dbd8dc1b024cc38287684346c01769/cb84b5c56bb1435c88c4e061ceae1b58/

#מו יש פה עוד הרבה היגיון בעניין, ולכן מומלץ לעיין עוד פה
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

#במקרה שלנו, אנחנו "ננקה" את המחרוזת שלנו מגורמים שלא מעניינים אותנו ורק אז נריץ את בדיקת הפלינדרום. בואו ננסח את זה בפסאודו-קוד:
#למה זה טוב? לפעמים אין לנו שליטה מלאה על הקלט של התוכניות אותן אנו כותבים.
# מאחר שברצוננו שהתוכנית שלנו תוכל לפעול על מגוון רחב ככל האפשר של קלטים, נרצה לעיתים לבצע התאמות לקלט שלנו לפני הרצת התוכנית.

#1. הסר רווחים מהמחרוזת st.
#
#2. הסר פסיקים מהמחרוזת st.
#
#3. הסר נקודות מהמחרוזת st.
#
#4. החלף את כל האותיות במחרוזת st לאותיות קטנות.
#
#5. הרץ את הפונקציה לזיהוי פלינדרום מהסעיף הקודם על המחרוזת החדשה והחזר את הערך שהתקבל.
#
# 1 כזכור לכם, על מנת להסיר תו מסוים מהמחרוזת ניתן להשתמש במתודה replace כאשר הפרמטר להחלפה הוא המחרוזת הריקה,
# למשל הקריאה st = st.replace("a","") תסיר מהמחרוזת את כל המופעים של התו "a"
# (שימו לב לכך שיש לבצע השמה חזרה למחרוזת st ולא להריץ את הפקודה replace בלבד!).
#
# 2. על מנת לשנות את כל האותיות במחרוזת לאותיות קטנות ניתן (ורצוי!) להשתמש במתודה lower של המחלקה str.
# נעשה זאת על ידי הקריאה st = st.lower()
# (גם כאן, שימו לב להשמה). מתודה זו משנה אותיות גדולות לקטנות ולא משפיעה על תווים שאינם אותיות.
#
# 3. לבסוף, את הסעיף האחרון בפסאודו-קוד נבצע על ידי קריאה לפונקציה אותה כתבנו בתרגיל הקודם.
# נדגיש כי אנו לא מעוניינים לכתוב בשלב זה מחדש קוד לבדיקה האם המחרוזת המתוקנת שלנו היא פלינדרום מושלם,
# מאחר וזו היא בעיה שכבר פתרנו!
# כלומר, לאחר "תיקון" המחרוזת, כל שנותר לנו הוא להריץ את הפקודה return is_palindrome(st).
# שימו לב כי מימשנו עבורכם את is_palindrome מהתרגיל הקודם בחלונית הקודבורד של התרגיל הנוכחי.
# כלומר לאחר שהפונקציה החדשה קיבלה מחזרות ושינתה אותה,
# אנחנו רוצים שהיא תזחיר את המחרוזת הזו עם הפעולה שבודקת פלינדרום מושלם, ובכך יצרנו פונקציה שבודקת פלינדרום רגיל
#
# 4. ניתן להניח כי אין במחרוזת סימני פיסוק מלבד רווחים, פסיקים ונקודות (כלומר, לא צריך לנקות מהמחרוזת סימני קריאה, שאלה וכו').
#
# אם אנחנו רוצים את זה יותר דינמי, יכול פשוט לבדוק קודם האם התו המבוקש מו]יע ברשימת התווים נניח: "!@#$%%^. ,:"
# for char in str:
#   if char in "!@#$%^&*(. ,:)"
# if char not in.....
#       st = st.replace(char,"")
# ואם כן אז להחליף אותו במחרוזת ריקה
# גם רווח הוא תו

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

