import functools
# 1.1.2

def double_letter(my_str):
       #return map(double,len(my_str))
    return "".join([p*2 for p in my_str])

print(double_letter("python"))
print(double_letter("we are the champions!"))


#1.1.3
def four_dividers(number):
     return number % 4 == 0

print(list(filter(four_dividers,range(9))))

#1.1.4

def add(a,b):
    return a+b

def sum_of_digits(num):
#    return functools.reduce(add,str(num),0)
    return sum(map(int, str(num)))

print(sum_of_digits(104))

