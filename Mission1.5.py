s1 = "Hans"
s2 = "Anna"
s3 = "Vladimir"
s4 = "Michael"
s5 = "Ed"
s6 = "Susan"
s7 = "Janice"
s8 = "Jo"

def max_name(s1,s2):
# כאשר זה בקובץ אפשר בעצם לעשות לולאה שרצה על הקובץ ומחזירה את הערך הגדול ביותר
# for i in file:
#    return max(i,i+1)
# או משהו דומה לזה
    return max(s1,s2)

print(max_name(s1,s2))
print(max(s1,s2,s3,s4,s5,s6,s7,s8))
print(max_name(s8,max_name(s7,max_name(s6,max_name(s5,max_name(s4,max_name(s3,max_name(s1,s2))))))))

print()

def sum_names(list):
    x = []
    for i in list:
        x.append(i)
    return sum((list))

# I moved to the next lesson
