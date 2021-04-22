# This part is actually form the pre course self.py - begining with python

#הפונקציה מקבלת כפרמטרים נתיבים של שני קבצי טקסט (מחרוזות).
# הפונקציה מחזירה אמת (True) אם הקבצים זהים בתוכנם, אחרת מחזירה שקר (False).
def are_files_equal(file1, file2):
    for i in file1:
        for j in file2:
            if i==j:
                return True
            else:
                return False
# ניתן גם לפתוח ולקרוא את שניהם ע"י read ולבדוק האם הם שווים למשל:
# if file2 in file1:

# https://www.geeksforgeeks.org/python-filecmp-cmp-method/
# with inbuilt function

# https://docs.python.org/3/library/filecmp.html
# from python document

# write new function for this
#for line1 in file1:
 #   for line2 in file2:
  #      if line1 == line2:
   #         FO.write("%s\n" %(line1))

# mission 1.5 rolling finale practice

file_object = open(r"C:\Users\חנן\Desktop\python\TestProject\NextPy\names.txt", "r")

#בכדי לקרוא את תוכן הקובץ כולו ניעזר במתודה ()read.
# המתודה מחזירה את תוכן הקובץ כולו כ מחרוזת אחת!!! שכוללת n\ בסוף כל שורה של הקובץ המקורי.

#read_file = file_object.read()
#print(read_file)

#מה החיסרון בקריאת תוכן של קובץ בעזרת המתודה ()read?
# הדוגמה לעיל מכילה קובץ טקסט קצרצר ובו ארבע שורות בלבד.
# לעומת זאת, בעבודה עם קבצים גדולים, השמה של תוכן קובץ לתוך משתנה יחיד עלולה ליצור עומס בזיכרון ולהאט את ריצת התוכנית.
# לפיכך המתודה ()read אינה מתאימה לקריאת קבצים גדולים

#              שימוש בלולאה למעבר על השורות ועל תוכן הקובץ

#בעבודה עם קבצים גדולים מומלץ להיעזר בשיטה אחרת: מעבר על שורה אחת בכל פעם, באמצעות לולאת for.
# בצורה זו נוכל גם להדפיס את הקובץ שורה אחר שורה:

# function that check the long string in the file, Iw've started it without putting it in a function, and then I have put it inside it.
def long_string_in_file (file):
    z = []
    # this to compare the length
    s = 0
    # to take the length and to put it in a string, and to be able to put the string in a variable that is initialiezed with "" to be 'string variable'
    t = ""
    n = 0
    for lines in file:
        print(lines,end="")
        z.append(lines)
        if s < len(lines):
            s = len(lines)
            t = lines
        n += len(lines)
        # we can use also the fun sum on the list z
    print()
    print(s)
    print("The long name is the file is:",t)
    print(z)
    print(n)

# לא ניתן להשתמש פה במעבר ע"י אינדקס ע"י range(len(file_object))
# כי נקבל:
#TypeError: object of type '_io.TextIOWrapper' has no len()
# זה לא מחרוזת
long_string_in_file(file_object)

#def short_string_in_file(file):
z = []
for line in file_object:
    print(line, end="")
    z.append(line)
    print(z)
    for j in z:
        res = min(len(j))
    print(res)
#short_string_in_file(file_object)

file_object.close()


def file_sort(f,name_func):
    lst = []
    for x in f:
        lst.append(x)
        if name_func == "sort":
            return sorted(lst)
#            mabey to use here split func, which saperate the string in to words and then to put/append them in a list
        elif name_func == "rev":
            return x[::-1]
        elif name_func == "last":
            n = 0
            input("Please Enter a number:", n)
            return f.lines(n)
            # return f.readline(n)
            # return f.readlines(n)
