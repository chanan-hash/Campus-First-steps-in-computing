# From the course "First steps in computing and python"
# 4.3.6

# regular search

def search_print(L, x):
    for e in L:
        if e == x:
            return True
    # if we got here the search failed
    return False
print()

# can add a counter to see how many iterations we had to do
def search_print_counter(L, x):
    count = 0
    for e in L:
        if e == x:
            print(f"The loop did {count} iterations")
            return True
        else:
            count += 1
    # if we got here the search failed
    return False


print()
# revers serch
def search_reverse(L, x):
    # delete pass and fill in your code below
    count = 0

    # we are starting the runnig from the end and going back every time one step backwards
    for e in range(len(L), 0, -1):
        if e == x:
            print("fount at:", count)
            return True
        else:
            count += 1
    print("found in the end of the list:", count)
    return False


L = [1, 2, 3, 4, 5, 6, 7]
x = 2
y = 8

print(search_reverse(L, x))
print(search_reverse(L, y))

print()

# serial search with the operator "in", which has more complicated implementantion algorithem and efficient, than regular serial search that we saw on the top of the code
def serial_search(L,x):
    if x in L:
        return True
    else:
        return False
