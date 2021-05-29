# From the course "First steps in computing and python"
# 4.5.3

# We must have the list sorted

# the complexity of binary search is close to log2(n) - which means, hoe many times we will need to divied n in 2, to get the number 1
# the same for 4 and 3 if we divieding the list into three or four parts ,log4(n)

# Regular binary search
def binary_search(L, x):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == L[mid]:
            # if we want to see the index place, we just need to return "mid"
            # we using the mid value to access the index
            # return mid
            return True
        else:
            if x < L[mid]:  # go to left half
                right = mid - 1
            else:  # go to right half
                left = mid + 1
    return False  # if we got here the search failed

lst = [3, 4, 5, 6, 9, 10, 13, 16, 18, 20, 22, 28, 29, 31, 32, 33, 40, 42, 47, 48, 50, 52]
result = binary_search(lst, 17)
print(result)
print(binary_search(lst,28))

print()

# Binary search with the valuse of "left, mid and right" every iteration
def binary_search_print(L, x):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        # add your print here!
        #print("left=", left, "mid=", mid, "right=", right)
        print(f"left= {left} mid= {mid}, right= {right}")
        if x == L[mid]:
            return True
        else:
            if x < L[mid]:  # go to left half
                right = mid - 1
            else:  # go to right half
                left = mid + 1

    return False  # if we got here the search failed


L = [1, 3, 7, 8, 10, 15, 16, 23, 25, 29, 31, 32, 35]  # an input list

print("********************")
print("Starting the test:")

for x in [3, 36]:
    print("*******************")
    print("L =", L, ", x =", x)
    print("--------------------")
    print("Your printouts:")
    binary_search_print(L, x)
    print("--------------------")

print()

# in which nine will it stop?
# it depends how does the right and left are moving and in what index it will find the nine
def binary_search2(L, x):
    count = 0
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        print("L[mide]:",L[mid], ", how many iteration has it done:", count, ", left:",left, ", it was found at index:", mid, ", right:",right)
        count += 1
        if x == L[mid]:
            return True
        else:
            count += 1
            if x < L[mid]:  # go to left half
                right = mid - 1
            else:  # go to right half
                left = mid + 1
        # it should be befor every iteration so we can get the valuse for the next iteration, and not for the previous one
        #print(L[mid],"how many iteration has it done:", count, left, "it was found at index:",mid, right)
    return False  # if we got here the search failed


# Test binary_search with lists that contains repeatitions
L = [1, 1, 2, 4, 6, 7, 7, 7, 8, 9, 9, 9]
print(binary_search2(L, 9))
print(binary_search2(L, 7))
print(binary_search2(L, 1))


# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/0abbdfc3b6b04237a1e9fa2bc58227b8/57af1623a6ac4c198ff33179dcc284c2/?child=first
# and there are all kind of searches in that course page

print()

# measuring time between linear search and binary search

# Linear search:
def search(L, x):
    for e in L:
        if e == x:
            return True
    # if we got here the search failed
    return False


# Binary search:
def binary_search(L, x):
    ''' search for x in L, which MUST BE SORTED !! '''
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == x:
            return True
        else:
            if L[mid] < x:  # go to right half
                left = mid + 1
            else:  # go to left half
                right = mid - 1

    return False  # if we got here the search failed


# Time measurements
import time  # the library time

for i in [1, 2, 4]:
    num_elems = 1000000 * i
    print("*** number of elements:", num_elems, "***")

    L = [i for i in range(num_elems)]  # a short way to generate the list [0,1,2,...,num_elems-1]

    # linear search
    start = time.clock()
    res = search(L, -1)  # res must be False, this is worst case running time
    end = time.clock()
    print("Linear search time:", end - start)

    # binary search
    start = time.clock()
    res = binary_search(L, -1)  # res must be False, this is worst case running time
    end = time.clock()
    print("Binary search time:", end - start)
    print()  # just a new line