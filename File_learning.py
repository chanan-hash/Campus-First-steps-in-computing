# This part is actually form the pre course self.py - begining with python

# The Func' gets as an argument two paths of files, as a string format
# The Func' returns True if both files identical in their content, else returns False

def are_files_equal(file1, file2):
    for i in file1:
        for j in file2:
            if i==j:
                return True
            else:
                return False
# if file2 in file1:

# https://www.geeksforgeeks.org/python-filecmp-cmp-method/
# with inbuilt function

# https://docs.python.org/3/library/filecmp.html
# from python document

# write new function for this
#for line1 in file1:
 #   for line2 in file2:
  #      if line1 == line2:
   #         FO.write("%s\n" %(line1))

# mission 1.5 rolling finale practice

file_object = open(r"C:\Users\חנן\Desktop\python\TestProject\NextPy\names.txt", "r")

#read_file = file_object.read()
#print(read_file)

# function that check the long string in the file, Iw've started it without putting it in a function, and then I have put it inside it.
def long_string_in_file (file):
    z = []
    # this to compare the length
    s = 0
    # to take the length and to put it in a string, and to be able to put the string in a variable that is initialiezed with "" to be 'string variable'
    t = ""
    n = 0
    for lines in file:
        print(lines,end="")
        z.append(lines)
        if s < len(lines):
            s = len(lines)
            t = lines
        n += len(lines)
        # we can use also the fun sum on the list z
    print()
    print(s)
    print("The long name is the file is:",t)
    print(z)
    print(n)

long_string_in_file(file_object)

#def short_string_in_file(file):
z = []
for line in file_object:
    print(line, end="")
    z.append(line)
    print(z)
    for j in z:
        res = min(len(j))
    print(res)
#short_string_in_file(file_object)

file_object.close()


def file_sort(f,name_func):
    lst = []
    for x in f:
        lst.append(x)
        if name_func == "sort":
            return sorted(lst)
#            mabey to use here split func, which saperate the string in to words and then to put/append them in a list
        elif name_func == "rev":
            return x[::-1]
        elif name_func == "last":
            n = 0
            input("Please Enter a number:", n)
            return f.lines(n)
            # return f.readline(n)
            # return f.readlines(n)

# for wrinting to a file go into:
# https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_selfpy101+1_2021/courseware/8dcc7c2d965247b0b8e7da1ea7956eb2/9986da15a56642678bac819e78448cf0/?child=first
# I didnt wan't to put it in here becuse I didn't want to create many file
# because if you want to write to file and it does not exist it will create a new one
# one of the important things to remembre in here is that it overrides the file if it exists. if we only waant just to write.
# it like create every time a new file withe the path name

# example
# file = open(file_name.txt,"w")
# file. write("some text")
# file. close()
# we can open a file and with a loop or read() func, to take the text and turn it to a string
# and to do some operations on the string with string functions
# and then to put/write it in the new file
print()
#  mission 9.2,2
def copy_file_content(source, destination):
    file_1 = open(source,"r")
    data = ""
    for read in file_1:
        data += read
    file_1.close()

    file_2 = open(destination,"w")
    file_2.write(data)
    file_2.close()
    return file_2

# mission 9.2.3

def who_is_missing(file_name):
    lst = []
    for i in file_name:
        lst.append(i)
        lst = sorted(lst)
        for j in range(lst[0], lst[-1] + 1):
            if j not in lst:
                return j

# we need to put a correct path here
    file_3 = open(r"found.txt","w")
    file_3.write("The missing number",j)
    file_3.close()