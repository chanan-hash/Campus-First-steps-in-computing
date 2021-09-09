# From the course "First steps in computing and python"
# 4.7.2

# The selection sort from Telusko works on tne understanding of "swap"
# This one works on creating a new list with removing the min value and appending it to a new kist, which will be sorted from the min to max
# on the oposite wat we cav remove the max valsue and then to creat a list from thr biggest to lowest valse

def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        #maximum = max(L)
        #L.remove(maximum)
        L.remove(minimum)
        sorted_L.append(minimum)

    return sorted_L

L = [1, 4, 5, 2, 3]
result = selection_sort(L)
print(result)

print()
# selection sort on the same way but usig max
# we are going to get sorted list from the lowest to the biggest but isted usig min() we we will use max()

def selection_sort2(L):
    # Write your solution here!
    n = len(L)
    sorted_L = []
    for i in range(n):
        maximum = max(L)
        L.remove(maximum)
        # if we want to append value to the list from the left and not from the right we can do something else than the func append
        # L = [x] + L
        # just to add the value in a square brackets into tha list, using the operator (+)
        sorted_L = [maximum] + sorted_L
    return sorted_L

import random

print("********************")
print("Starting the test:")
print("Note: we test your function on 3 RANDOM lists with 7 items each")
for i in range(3):
    print("********************")
    # randit func taking numbers between the range we gave the, but randomly
    # and with list comprehention we out the random value in a loop in range of 7 times
    # in the end we getting list with 7 random numbers between 1-100 in a list
    L = [random.randint(1, 100) for j in range(7)]
    print("Testing the following list:", L)
    if sorted(L) == selection_sort2(L[:]):  # pass a copy of L to selection_sort2
        print("CORRECT: Very good, the sorted list is:", sorted(L))
    else:
        print("WRONG: your answer is:", selection_sort2(L[:]), ", but the correct answer is:", sorted(L))

print("********************")
print()

# The complexebilty of selection sort

import random
import time

def generate_random_list(n):
    ''' returns a list of size n with random integers between 0 and 999999
        Uses random.randint(a,b) which randomly picks an integer between a and b
    '''
# and the lenghth of the list is going to be n, and the values in the list itself eill be number between 0 - 999999
    # that means, that if n us equal to 1000, we will have a list with 1000 values between 0 - 999999
    return [random.randint(0, 999999) for i in range(n)]  # a short way to generate the list

def selection_sort(L):
    ''' return a sorted copy of L '''
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)
    return sorted_L

for n in [1000, 2000, 4000]:
    lst = generate_random_list(n)

    start = time.clock()
    lst2 = selection_sort(lst)  # lst2 not used
    end = time.clock()

   # if we want to see the list itself, and the values in the list
   # print(lst2)
    print("Number of elements in the list: ", n)
    print("Time measured for selection_sort: ", end - start, " seconds")
    print()  # just a new line

# and if we use the inbuilt function "sorted" it will reduce the compelxibility significantly

y = 100000
lst = generate_random_list(y)

start = time.clock()
lst3 = sorted(lst) # lst3 not used
end = time.clock()

# fron the Test on end of lesson four, questoin 7:
# Function that chacks if the list is sorted

print()

def is_sorted(lst):
    # delete pass and fill in your code below
    # we checking the negative way
    # if we have a problem return false.
    # we aren't checking if the cindition is true
    # if the condition don't happen, means - if it isn't returning false
    # so return true
    for i in range(len(lst) - 2):
        #if lst[i+1]<lst[i]:
        if lst[i] > lst[i + 1]:
            return False
    return True

# using in built function
def is_sorted2(L):
    return L == sorted(L)
# we can use a condition
# if L == sorted(L):
# return True
# else: return False

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Check if [2, 3, 4] is sorted")
ans = is_sorted([2, 3, 4])
if ans == True:
    print("CORRECT: [2, 3, 4] is sorted")
else:
    print("WRONG: [2, 3, 4] is sorted but your code returned", ans)

print("********************")
print("Check if [2, 1, 4] is sorted")
ans = is_sorted([2, 1, 4])
if ans == False:
    print("CORRECT: [2, 1, 4] is not sorted")
else:
    print("WRONG: [2, 1, 4] is not sorted but your code returned", ans)

### EXTRA TESTS ###
### DO NOT MODIFY THIS PART ###
### THESE TESTS CHECK IF YOUR SOLUTION FOLLOWS THE GUIDELINES ###

import inspect
import ast

def no_sorted(f):
    call_names = [c.func.id for c in ast.walk(ast.parse(inspect.getsource(f)))
                  if hasattr(c, 'func') and hasattr(c.func, 'id') and isinstance(c, ast.Call)]
    return not 'sorted' in call_names

print("********************")
print("\n\nNow checking your implementation:")
if no_sorted(is_sorted) == True:
    print("CORRECT: Your function does not call the builtin sorted function")
else:
    print("WRONG: Your function calls the builtin sorted function")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

print()

# # fron the Test on end of lesson four, questoin 10:
# we want to find the min element, for k number
# for example - [6, 8, 2, 4, 5] and k = 3
# we will get 5
# we depending on the psa-code:
# in the link question 10
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/0abbdfc3b6b04237a1e9fa2bc58227b8/27a0ec43965b46fd8b5d59f64f7af6a6/?child=first

def kth_element(lst, k):
    # delete pass and fill in your code below
    for i in range(k-1):
    #because we want the length until k, not included
        lst.remove(min(lst))
    return min(lst)

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Finding the first element in [7, 6, 5]")
ans = kth_element([7, 6, 5], 1)
if ans == 5:
    print("CORRECT: 5 is the first-in-size element in [7, 6, 5]")
else:
    print("WRONG: 5 is the first-in-size element in [7, 6, 5] but your code returned", ans)

print("********************")
print("Finding the second element in [7, 6, 5]")
ans = kth_element([7, 6, 5], 2)
if ans == 6:
    print("CORRECT: 6 is the second-in-size element in [7, 6, 5]")
else:
    print("WRONG: 6 is the second-in-size element in [7, 6, 5] but your code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")