import functools

#MAP

for num in range (1,20):
    string = ""
    if num % 3 ==0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 3 !=0 and num % 5 !=0:
        string = string + str(num)
    print(string)

print()

def combine_coins(coin,number):
    output = ''
    for i in number:
        output += coin + str(i) + ','
# ignore the last comma.
    return output[:-1]

print (combine_coins("$",[1,2,3,4]))

print()

def squre (num):
    return num **2

list1 = [2,3,4,5,6]
new_list = []

for number in list1:
    new_list.append(squre(number))

print(new_list)

result = map(squre,list1)
print(result)
print(list(result))

print()

print("Map:")
def magic(a, b):
    return a * b
list_one = [1, 2, -5, 6]
list_two = [2, -1, 3, 4]
print(list(map(magic, list_one, list_two)))

print()
print("Filter:")

#Filter and Reduce

#Filter

def func(x):
    return x % 2 != 0
print(list(filter(func, range(10))))

print()
print("Reduce:")

#Reduce

def add (x,y):
    return x + y

shop_list = [200, 120,330,50]
print(functools.reduce(add,shop_list))

def f(a, b):
    if a < b:
        return a
    else:
        return b
# the functions returns the lowest value
print(functools.reduce(f, [47,11,42,102,13]))
# in the first time it will be 11
# the f = 11
# and actully it will remain the lowest values in the whole list

# initializer