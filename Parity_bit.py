# From the course "First steps in computing and python"
# 5.3
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/827e6ce27709464a820b2753d1e95f46/?child=first

# Checking for an error by "even bit"

# we asking from python, to sum the char  "1" in the series, and return the modulu by to, for even/odd

def parity(string):
    par = 0
    for chr in string:
# we aren't we writing - if chr == 1, with out a string? try and check it.
# because then the Func' will allways return 0, beccause it is getting a string, and there won't be there any number, so par == 0
# and the modulu of 0 % 2, is 0.
# we looking for the char "1", and not the number. at least the computer looking for it, although tjat actually we want the number
        if chr == "1":
            par = par + 1
    return par % 2

# Call parity with various binary strings, i.e. - strings made up of "0"s and "1"s

print(parity("0100101010101011100"))
print(parity("01001010101010111001"))
