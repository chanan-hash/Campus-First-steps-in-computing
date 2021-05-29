import math
# this I added way more later, to put it in a loop that we can to it as mauch time as we want
# we can do prime number like this

# while True:
  #  x = int(input("Enter a number: "))

   # for i in range(2, x // 2):
    #    if x % i == 0:
     #       print("Not a prime  number")
      #      break
       # else:
        #    print("Prime number")


# or we can put it in a function to find the smallest factor of the number which will be a prime number
# we can write 12 = 3*4 or 12 = 2*2*3
# and ten every factor is a prime number

# בתרגול זה אתם מתבקשים לכתוב תוכנית למציאת הגורם הראשוני המינימלי של מספר שלם.
# הנה תזכורת לפסאודו-קוד של התוכנית שהוצג ביחידה על מספרים ראשוניים:

# קלט: מספר שלם חיובי n

# 1. לכל k בין 2 לבין n:

# 1.1. אם n מתחלק ב-k ללא שארית:

# 1.1.1. החזר את k וסיים (k הוא הגורם הקטן ביותר של n)

# בחלונית הקודבורד שלפניכם תמצאו את כותרת הפונקציה smallest_factor(n).
# הפונקציה מקבלת כקלט מספר שלם חיובי n. עליה להחזיר את k, המספר השלם הקטן ביותר בין 2 ו-n אשר מחלק את n ללא שארית.

def smallest_factor2(n):
    # delete pass and fill in your code below
    for k in range(2,n+1):
        if n%k==0:
            return k

# more effective way to the algorithem
def smallest_factor(n):
    # we will do only sqrt iteration for n, with while loop
    # for the explanation read here, 3.5.7:
    # https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/63dbd8dc1b024cc38287684346c01769/22c5c1fceea8469d88cdc52bb055ae05/?child=first

    k = 2
    # k must start form 2, or must be initailized with 2, because this is the first factor we can check, 1 will not help us
    # because 1, can be all ways be a factor to any number we want, and 0, will make us to divied a number with 0, and this is an error
    while k < math.sqrt(n):
        if n%k==0:
            return k
        else:
            k += 1



print("********************")
print("Checking the smallest factor of 33")
ans = smallest_factor(33)
if ans == 3:
    print("CORRECT: 3 is the smallest factor of 33")
else:
    print("WRONG: 3 is the smallest factor of 33 but the code returned", ans)

print("********************")
print("Checking the smallest factor of 17")
ans = smallest_factor(17)
if ans == 17:
    print("CORRECT: 17 is the smallest factor of 17")
else:
    print("WRONG: 17 is the smallest factor of 17 but the code returned", ans)
