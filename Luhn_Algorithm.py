# From the course "First steps in computing and python"
# 5.2.2
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/2319486f6102498ca12f4fcf269f0e94/?child=first

# Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers (from wikipedia)
# https://en.wikipedia.org/wiki/Luhn_algorithm
# https://he.wikipedia.org/wiki/%D7%A1%D7%A4%D7%A8%D7%AA_%D7%91%D7%99%D7%A7%D7%95%D7%A8%D7%AA

# This func' will return your identification number
# ID - needs to be a String
def control_digit(ID):
    # variable to save the sum of the ID
    s = 0
    for i in range(8):
        # converting the string into a number
        # taking tje character in the index 'i', which will be a number but as a char, and converting it to a number so we can do math operation on it
        digit = int(ID[i])
        # in the even place of the string, we just adding them to the sum
        if i % 2 == 0:  # i is one of 0,2,4,6 - index
            s = s + digit
        # the odd places
        else:  # i is one of 1,3,5,7 - index
            digit = digit * 2
            if digit <= 9:
                # in the Luhn algorithm after we double the nubmer we beed to add it to the sum as a single number
                s = s + digit
            # if after we multiplie it the number is bigger than 9, like 10, 16, 15/ we need some how to separte the to 15 = 1+5/ 10 = 1+0.. and then to add them to the sum
            else:
                # modulu with 10, will give us the ones number, 16%10 = 6
                # and than we need just to add 1. it will always be "1", because, to get n*2 = 20, n must be 10, and the biggest digit is 9, and if we multiplie it by itself it will give us 18. so 18 will be the biggest number we need (if we'll need) to separte and add to the sum)
                ones = digit % 10
                tens = 1  # digit is one of 10, 12, 14, 16, or 18
                s = s + tens + ones
    # we override the previouse 'ones', and putting there the the "ones" of the sum, so we will be able to use it for checking the "check digit"
    ones = s % 10
   # we taking the new "ones" and Subtract it from 10
    check_digit = 10 - ones  # the number we want to find - 'check digit'
    # handling with Extreme case if the sum become a number which can be divided by 10, such as s = 40, so the 'ones' equal to 0
    # and then 10 - 0 = 10, and the check_digit can't be to numbers onlt a one, Other what is the point of the check_digit
    # that why we adding a condition for the calculating
    # for an Explanation see here, part 3, the last tab:
    # https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/2319486f6102498ca12f4fcf269f0e94/?child=first
    if check_digit == 10:
        check_digit = 0

    return check_digit

# Change the current ID and run the code!
print(control_digit("12345678"))
print(control_digit("73908547"))
# explanation on the code
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/8930998f65ab4226bf548730b63302fd/2319486f6102498ca12f4fcf269f0e94/?child=first