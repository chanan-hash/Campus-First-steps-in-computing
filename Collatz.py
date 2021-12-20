# From the course "First steps in computing and python"
# 8.4

# That function is taking a natural/integer number
def collatz(n):
    """ runs the 3n+1 iteration and prints each element till
        1 is reached. Will not halt if 1 is never reached """
    initial = n
    print(initial)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)

    # if we got here, n must be 1
    print("halted on input", initial)

#collatz(17)
#collatz(512)
#collatz(1048576)
#collatz(2**30)
#collatz(2**30+1)
#collatz(2**50)
collatz(2**50+1)

print()

# counting the iterations

# Modify the code below to return the number of iterations the for-loop performed
# Tip: You may want to remove all print commands so the output is more readable.
def collatz(n):
    """ runs the 3n+1 iteration and prints each element till
        1 is reached. Will not halt if 1 is never reached """
    initial = n
    count = 0 # to count the iterations we will just add\make a counter and every iterations we will add him +1, and in the end we'll return him
    print(initial)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            #count = count + 1
        else:
            n = 3 * n + 1
            #count += 1
        print(n)
        count += 1
        # if we got here, n must be 1
    print("halted on input", initial)

    return count


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking n = 17")
ans = collatz(17)
if ans == 12:
    print("CORRECT: 17 terminates after 12 iterations")
else:
    print("WRONG: 17 terminates after 12 iterations but the code returned", ans)

print("********************")
print("Checking n = 1987623")
ans = collatz(1987623)
if ans == 122:
    print("CORRECT: 1987623 terminates after 122 iterations")
else:
    print("WRONG: 1987623 terminates after 122 iterations but the code returned", ans)

print("********************")
print("Checking n = 1")
ans = collatz(1)
if ans == 0:
    print("CORRECT: 1 terminates after 0 iterations")
else:
    print("WRONG: 1 terminates after 0 iterations but the code returned", ans)

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

