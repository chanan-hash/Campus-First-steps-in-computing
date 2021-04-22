# מהקורס צעדים ראשונים בתכנות ובמדעי המחשב
# שיעור 3 לולאות 3.4.12
# תרגיל רשות, הגרלות של מספר אקראי של תאריכים עד התאריך הנכון

#כפי שודאי שמתם לב, זהו תרגיל דומה למה שראינו בסרטון, אלא שכאן נדרשים שני תנאים - צריך שתהיה התאמה בין התאריך שהוגרל לתאריך הקלט גם ביום וגם בחודש.
# במילים אחרות - כל עוד היום שהוגרל שונה מיום הקלט או החודש שהוגרל שונה מחודש הקלט - נמשיך להגריל תאריכים.
# לצורך כך ניזכר במילה or בפייתון בה כבר נתקלנו כשלמדנו על ביטויי תנאי מורכבים. נסביר שוב בקצרה איך היא עובדת באמצעות שורת הקוד הבאה:
# while condition1 or condition2:
#כאשר condition1 ו-condition2 הם שמות תנאים בוליאניים כלליים (כלומר, ביטויים שערכם הוא True או False, כגון 3 > 5, 6 =! 7 וכו').
# אנו מתייחסים לביטוי condition1 or condition2   כתנאי בוליאני בפני עצמו, התלוי בשני החלקים הללו - התנאי משוערך ל-True כאשר לפחות אחד מהתנאים משוערך ל-True, ומנגד, משוערך ל-False אך ורק אם שני התנאים הללו משוערכים ל-False

import random

def count_rolls_until_6():
    res = random.choice([1, 2, 3, 4, 5, 6])
    # print(res)
    count_rolls = 1
    while res != 6:
        res = random.choice([1, 2, 3, 4, 5, 6])
        # print(res)
        count_rolls = count_rolls + 1

    return count_rolls


days = [i for i in range(1, 32)]
months = [i for i in range(1, 13)]


def birthday(day, month):
    # Write your solution here
    bdd = random.choice(days)
    bdm = random.choice(months)
    print(bdd)
    print(bdm)

    count_try = 0

    while bdd != day or bdm != month:
    # כלומר כל עוד זה לא שווה או זה לא שווה - זה כמו הצד ההפוך/המד השולל של כאשר אלה שווים
    # לפעמים יותר טוב/קל להגדיר תנאי על פי השלילה שלו כמו שכבר ראינו בקורס הזה באמצע הנושא של לולאת for על range. מומלץ מאוד ראות ולהזכר שם בתרגיל בסוף
        bdd = random.choice(days)
        bdm = random.choice(months)
        print(bdd)
        print(bdm)

        count_try += 1

    return count_try


day = 1
month = 1
print("It took", birthday(day, month), "trials to draw this birthday:", day, ".", month)