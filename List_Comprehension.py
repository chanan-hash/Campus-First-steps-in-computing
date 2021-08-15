my_money_list =[]
for i in range(100):
    my_money_list.append(i**2)
print(my_money_list)

my_money_list2 = [2,4,5,6,7,8]
def sqr(n):
    return n**2
print(list(map(sqr,my_money_list2)))

my_money_list3 = [x**2 for x in range(100)]

print(my_money_list3)

print()

letters = ['a','b','c']
upper_letters = [x.upper() for x in letters]
print(upper_letters)

print()

list1 = [1,2,3]
list2 = [5,6,7]

# the regular way:
mult_list = []
for x in list1:
    for y in list2:
        mult_list.append(x*y)
print(mult_list)

mult_list2 = [x*y for x in list1 for y in list2]
print(mult_list2)

print()

my_list = [1,2,3,4,5]
squared_list = [x*x for x in my_list if x%2==0]
print(squared_list)

print()

nested_list = [x*2 for x in range(10) if x>3 if x<7]
print(nested_list)

print()

Even_Odd_list = ["Even" if i % 2 ==0 else "Odd" for i in range(10)]
print(Even_Odd_list)

print()

number = [1,2,3,4]
list_of_lists = [[2*x,x] for x in number]
print(list_of_lists)

print()

sentence = "the quick brown fox"
words = sentence.split()
print(words)
secret = [word[0] for word in words if word != "the"]
print(secret)

print("The coin challange: ")

combine_coins = [list(map(lambda coin,number : coin + str(number) + ',','$',range(5)))]
print(combine_coins)
#print(combine_coins('$',range(5)))

def combine_coins2 (coins,numbers):
    return ','.join(map(lambda s,n: s+ str(n) ,[coins for i in numbers], numbers))

print(combine_coins2('$',range(5)))

print()

power_3_list = []
for i in range(100):
    power_3_list.append((i**3))
print(power_3_list)

#בעזרת map
def power_3(x):
    return x**3
print(list(map(power_3,range(100))))

# בעזרת הרכבת רשימה
power_3_list2 = [i**3 for i in range(100)]
print(power_3_list2)

print()
'''new_list = [expression for item in sequence]'''

'''new_list = []
for item in sequence:
    new_list.append(expression)'''

print()

letters = ['a', 'b', 'c']
upper_letters = [x.upper() for x in letters]
print(upper_letters)

print()

#result = [expression for item1 in sequence1 for item2 in sequence2 ]

#regular way:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
mult_list = []
for x in list1:
     for y in list2:
        mult_list.append( x * y )
print(mult_list)

# The short way:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
mult_list = [x * y for x in list1 for y in list2]
print(mult_list)

print()

#result = [expression for item in sequence if condition]

my_list = [1, 2, 3, 4, 5]
squared_list = [x * x for x in my_list if x % 2 == 0 ]
print(squared_list)

nested_list = [x * 2 for x in range(10) if x > 3 if x < 7]
print(nested_list)

print()

#result = [ expression1 if condition else expression2 for item in sequence]

even_odd_list = [ "Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(even_odd_list)

print()

numbers = [1, 2, 3, 4]
list_of_lists = [ [2 * x, x] for x in numbers]
print(list_of_lists)

print()
sentence = "the quick brown fox"
words = sentence.split()
secret = [word[0] for word in words if word != "the"]
print(secret)