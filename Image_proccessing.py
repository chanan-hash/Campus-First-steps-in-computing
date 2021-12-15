# 7.3.2
from PIL import Image
#import IP

# open image
img = Image.open("example.jpg")
#img.show() - # it is like print
#print(img.size)
img2 = img.resize((100,100))
#img2.show()
img3 = img.convert('L') # convert it to gray format, when every pixel is on the same bits/number in RGB
#img3.show()
mat = img3.load() # calling the matrix that presenting the picture, means the option to access a specific pixel
#print(mat[10,20])
mat[10,20] = 255
#print(mat[10,20])
# for x in range(50):   # chaning few pixel into another color, insted of one
#     for y in range(50):
#         mat[x,y] = 255
# img3.show()

# for x in range(50):
#     for y in range(50):
#         mat[x,y] = 300
# img3.show()

# creat a new image - this function getting 3 argument: 1- the color format, 2- the size, 3- the color of the pixel (in gray format it's only one number for all RGB)
img4 = Image.new('L', (100,50), 128)
img4.show()

print()

# 7.3.3
from PIL import Image
# import IP

# Modify this code:
img = Image.open("example.jpg")
img = img.convert('L')
mat = img.load()

# changing the down-left corner of the picture into a square of gray color
# row\width
for x in range(150,200):
  # coloum\height
    for y in range(100,150):
        mat[x,y] = 128
img.show()

# shoe=wing thr image size
w, h = img.size
print(w,h)
print()

# 7.4.1
from PIL import Image
# import IP

img = Image.open("example.jpg")
img = img.convert('L')
#img.show()

# this function slices a rectangle from th picture
slice = img.crop((30,20,80,80)) # the firs to coordinates are the up-left corner, and the next to second numbers are the down-right coordinates - (x1,y1,x2,y2)
#slice.show()
img2 = img.rotate(-90) # the parameter which is given is the angle we want to ratate the picture counterclockwise
# To rotate it clockwise we need to give the function a negative number
#img2.show()
# this function is giving us the numbers of pixel in each color from 0-255, like how many black pixels we have, etc.
hist = img.histogram()
print(hist) # it is a list type
# if we want to see how many pixels we have in a specific number we will just neet to access it by it index (bright gray = 200)
print(hist[200]) # because we starting from 0 till 255

#IP.save_image_from_url("https://image.ibb.co/dq07dL/duck.jpg", "donald.jpg")
#img1 = Image.open("donald.jpg")
#img1.show()


# 7.5.2
# Function on the picture is actually pixel manipulate
# making the picture brighter or darker depending on the given "k" which we will add to the pixel number value
def add(im, k):
    w, h = im.size # the two variable taking the original image size
    im_new = im.copy() # we are making a copy that we won't hurt the original image
    mat_new = im_new.load() # loading the pixel matrix

    for x in range(w):
        for y in range(h):
            mat_new[x, y] = mat_new[x, y] + k # if k is positive - the picture will become brighter, and if it is negative it will be darker
    return im_new

img.show(add(img,50))

# The same Func' but with condition if the value of the pixel will become more than 255 or less than 0

def add(im, k):
    w, h = im.size # the two variable taking the original image size
    im_new = im.copy() # we are making a copy that we won't hurt the original image
    mat_new = im_new.load() # loading the pixel matrix

    for x in range(w):
        for y in range(h):
            mat_new[x, y] = mat_new[x, y] + k # if k is positive - the picture will become brighter, and if it is negative it will be darker
            if mat_new[x, y] > 255:
                mat_new[x, y] = 255
            elif mat_new[x, y] < 0: # if mat_new[x, y] < 0:
                mat_new[x, y] = 0
    return im_new


# negative of a picture
# how do we do that? black pixel (0) will be changed with a white one (255) and the oposite. but what with a pixel that is value is 1?
# it will be change to 254, 2->253 3->252... all in around of 255, what that comlete it to 255
# every pixel chnges in the same pixel that is in the same distance but from the other side. exm: 1 is a one step from 0, and 254 is one step from 255, so thay will be changed one in the other
# in another words if the value of the pixel is "a" so the new value to negative and chang it will be -> "255-a"

def negate(im):
    w, h = im.size
    im_new = im.copy()
    mat_new = im_new.load()

    for x in (w):
        for y in (h):
            a = mat_new[x,y] # 'a' getting the current value of the pixel
            mat_new[x,y] = 255 - a # we are changing that pixel to '255 - a'
            # we could write it in one line without the variable 'a' --> mat_new[x,y] = 255 - mat_new[x,y]

    return im_new


# 7.5.3
# turnning picture upside_down
# from PIL import Image
# import IP

img = Image.open("example.jpg")
img = img.convert('L')

def upside_down(im):
    w, h = im.size
    im_new = Image.new('L', (w, h), 255) # creating a new white image the same size as the older image
    mat = im.load() # older img matrix
    mat_new = im_new.load() # new img matrix
    for x in range(w):
        for y in range(h):
            mat_new[x, y] = mat[x, h - y - 1] #the new matrix will be the upside_down of the older img matrix
            # if we want to turn the picture form left to right, insted changing y\the row, we would change the column\x
            # mat_new[x, y] = mat[w - x- 1, y]
            # mat_new[x, y] = mat[w - x- 1, h - y - 1] - upside_down and left_to_right
            # it is just playing with the matrix
    return im_new

# insted doing it on a copy of the older picture we did it on a new one
# becuse if we won't do it on a new imagw which we have created, the picture will be cut to 2, and one half will be upside and the other won't
# in the beggining we starting to turn the picture upside, from down-left pixels. then when the we are getting to the up-left pixel we are turning again the picture so we have only half picture.
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/e395874321314eabb63db32a500b3a22/06104478f60747aeaea50748cf845262/?child=first
# 7.5.4 there is an explanation what is happening if we aren't making a new image, only a copy - why it won't work

img.show()
img2 = upside_down(img)
img2.show()


# 7.6.2
# artificial image - creating a diagonal

def diagonal(n):
    im = Image.new('L', (n, n), 255)
    mat = im.load()
    for x in range(n):
        for y in range(n):
            if x - y == 0: # or like this --> if x == y:
                # if we want to move the pixel to the right we'll write - if x-50 == y: --> the pixel will move 50 steps to the right, the one that will be colored are the one which the row is bigger by 50 from the column. ex': [50,0] [51,1] [52,2] etc
                # the same way if we want to start lower - if x+50 == y --> the pixel will move 50 steps lower, the one that will be colored are the one which the column is bigger by 50 from the row. ex': [0,50] [1,51] [2,52] etc

            # 1) if x>y: --> we'll get the firts row
            # 2) if x<y: --> we'll get a triangle on the down-left side. all the pixels that the number of column is smaller than the number of the row. [0,1], [0,2][1,2], [0,3][1,2][2,3], etc...
            # 3) if x+y==200 --> we'll get the other way digonal, from up-right to down-left
            # 4) if x*y//2==0 --> we'll get half of the frame, the up and left frame
                mat[x, y] = 0
    return im

img = diagonal(200)
img.show()


# 7.6.3
# stripes picture

# The four codes lines in the begining of the function are the same as we've seen
# creating a new white "board"/image
# uploading the matrix that we'll be able to manipulate the pixels and work and change them
# then going through them by nested loop
def stripes(n):
    im = Image.new('L', (n, n), 255)
    mat = im.load()
    for x in range(n):
        for y in range(n):
            if x % 10 == 0: # every pixel in the column that is a double of 10 [10,0][20,0][30,0].....[10,1][20,1]....[10,2][20,20]...etc
            #if x % 20 == 0: --> that if we wnat to widen the space between every stripe, and to reduce the number of stripes by 2. To do it by three it will be --> if x % 30 == 0... etc.
            # x%10 == 0 ב־x%10 == 0 or x%10 == 1: --> that if we want to make the stripes thicker, because here we are blacken column 0,1,10,11,20,21... etc insted only 0,10,20. we are actualy adding another stripe that is linked the frst stripe
                mat[x, y] = 0 # coloring in black
    return im

stripes(200).show() # we've got a trips picture. we have colored only the columns, only x

# to make the function be with less complexability we - now we are gion over every pixel and checking the codition. most of the pixel we aren't need to color
# so it turns out that we are going over 200x200 pixel = 400,000.
# insted we can put the condition befor the second loop, and then only if the column standing in the condition, means if the column is a double of 10 (0,10,20...)only then we are going into the row and coloring it
# turns out we will color/blcken only 20 column (200/10 = 20) --> 20 column x 200 rows = 20*200 = 4,000!!!
# ten precent (10%) less than the begining!!

# The function will lokk like this:
def stripes(n):
    im = Image.new('L', (n, n), 255)
    mat = im.load()
    for x in range(n):
        if x%10 == 0: # !!!!! <-----
            for y in range(n):
                mat[x, y] = 0
    return im

stripes(200).show()


# 7.6.5
# a special function that plays a little bit with the pixels

def product(n):
    surprise = Image.new('L', (n, n), 255)
    mat = surprise.load()

    for x in range(n):
        for y in range(n):
            mat[x, y] = (x*y) % 256 # try to guess what will happen.
        # we are mupltiply the number value of x with the value of y, to get a number and then we are doing modulu with 256 - the number we are getting is the color that tge pixel will be colored.
    return surprise

img = product(256)
img.show()

print()

# in the same way another function as product but it is different in the coloring line
def circles(n):
    surprise = Image.new('L', (n, n), 255)
    mat = surprise.load()

    for x in range(n):
        for y in range(n):
            mat[x, y] = (x**2 + y**2) % 256

    return surprise

img = circles(256)
img.show()

# this one, one of the students did, just play with the function :)

def circles(n):
    surprise = Image.new('RGB', (n, n),(134,35,45)) # he used 'RGB' format and not gray format
    mat = surprise.load()

    for x in range(n):
        for y in range(n):
            # here we are making the change in each color of an argumet that we've created, and than putting it in the matrix
            r=(2376*5+x**y)%256
            g=(2376**5+y-x)%256
            b=(23+x//456+y)%256
            mat[x, y] = (r,g,b)

    return surprise

img = circles(256)
img.show()


# 7.7.1
# noise handling\cleaning

# creating salt and pepper noise on a picture
#from PIL import Image
#import IP

import random


def add_sp(img, p):
    w, h = img.size
    mat = img.load()  # we don't realy need the original image matrix
    noisy_img = img.copy()
    noisy_mat = noisy_img.load()
    for x in range(w):
        for y in range(h):
            # we are creating the probability
            r = random.random()
            if r < p:
                # half of it is white and half of the probability is black
                if r < p / 2:
                    noisy_mat[x, y] = 0  # making\changing the color of the pixel and that make the noise\salt-pepper
                else:
                    noisy_mat[x, y] = 255

    return noisy_img


img = Image.open("example.jpg")
img = img.convert('L')

p = 0.1  # try different values
noisy = add_sp(img, p)
noisy.show()


# To clean the noises we need will do it by focusing in to qualities:
# 1 - because the noises are randomaly it likely to be that its the only pixel in his area that had been changed
# 2 - in most of the picture the values of the pixel dosen't change so extreme (form 59 suddenly to 255)
# so tha algorithm will go over every pixel aand decide if it had been beaten by 'salt-pepper noise', by chacking his value:
# if: it not extreme such as 255 or 0, we won't change that pixel.
# else: we will change that pixel. but how? we will change his value according to his area, that for us it will be a square of 3X3 (a litte matrix), and the pixl we want to change will be in the middle.

# so to fix it we need do have three preparations:
# 1 - we need to understand how we are focusing python on a little part of the image\picture
# 2 - that focuse will lead us to a little matrix of 3X3, that we want to "flatten" it to a list - form 2D object (3X3) to a 1D object (list with 9 arguments)
# 3 - in the end we need to determine the value that features the close enviroment of the pixel. that we will do by taking the flatten matrix and finding the  median of the 9 pixels


# making the focused area in the matrix (3X3) and adding them to a list
# we are goimg ovewr every pixel by a nested loop, one for the column and one for the row, and adding them, to a emptty list
def items(mat, x, y):
    # flatten 3-by-3 square elements around mat[x,y] into a list
    lst = []
    # to anderstand how the loop works we can draw it what is happening in every itteration
    for a in range(x-1,x+2): # going over the three rows
        for b in range(y-1,y+2): # going over the three columns
			lst.append(mat[a,b]) # adding the cross\meeting point of the rows and columns
#       X-1   x   x+2
# Y+1    *    *     *

# Y      *    *     *

# Y+2    *    *     *

    return lst


# finding the median
# median is a number that half of the numbers are bigger than him, and the other half is smaller, 1,29,3,30,100 --> sorted = 1,3,29,30,100
# the median here is 29, it is not the avrage. that why the median is not effected from extreme values, an important attribute for cleaning salt-pepper noise
# if the list has a odd numbers of places so it is easy to find the median, but is the list has a even numbers of values so we can take of of the tow median or the avarage between them

def median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    return sorted_lst[n//2] # the index of the middles\median number of the list


# the cleaning algorithm
# we are copping the the picture that the original value won't get "hurt"
# we are going over every pixel that is not on the edge/frame - because those pixel doesn't have aaround them square of 3X3
# it is enough to get a cleaner picture than before despite the frame can be still with noises

# if we will go over the whole matrix\pixels we will get an error --> "IndexError: image index out of range" --> this will be, for x in range(w): for y in range (h):

def clean_sp(img):
    # cleans salt and pepper noise from mat
    w, h = img.size
    mat = img.load()

    clean_img = img.copy()
    clean_mat = clean_img.load()
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if (mat[x, y] == 0) or (mat[x, y] == 255):  # needs cleaning
                clean_mat[x, y] = median(items(mat, x, y))

    return clean_img


# exam lesseaon 7 question 5
def what(n):
   img = Image.new('L',(n,n),'white')
   mat = img.load()
   for x in range(n):
       for y in range(n):
           if x-y == 0 or x+y == n-1: # the first condition is to get the top left digonal, and the second condition is to get the top right digonal
            # in the second condition we are lokking for the pixel in the matrix that will give the sum of n (n-1, because we are counting from 0, so 5 is 0,1,2,3,4)
               mat[x,y] = 0 #0 is black

   return img

what(5).show()
# what will we get?

import urllib
import random

def display_image(im):
    fn = str(random.randint(1, 500)) + ".bmp"
    im.save(fn)
    print("<img src=\"/resources/{}\">".format(fn))
    print("")

Image.Image.show = display_image


# qu 7
# making chess board
def chess(n):
    im = Image.new('L',(n,n),255)
    mat = im.load()
    for x in range(n):
        for y in range(n):
            if (x + y)%2 == 0:
            # if we will take every pixel\cordinate in the matrix that is neede to be colored in black,
            # we will see that the common ground is that the sum of x & y is even
                mat[x,y] = 0
    return im

chess(8).show()


print("********************")
print("Starting the test:")

print("********************")
print("Checking for n = 2")
ans = chess(2)
test = [0, 255, 255, 0]
if type(ans) == Image.Image and list(ans.getdata()) == test:
    print("CORRECT: A proper chess board was drawn for n = 2")
else:
    print("WRONG: An improper chess board was drawn for n = 2")

print("********************")
print("Checking for n = 3")
ans = chess(3)
test = [0, 255, 0, 255, 0, 255, 0, 255, 0]
if type(ans) == Image.Image and list(ans.getdata()) == test:
    print("CORRECT: A proper chess board was drawn for n = 3")
else:
    print("WRONG: An improper chess board was drawn for n = 3")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")


# creating a black frame
def border(n):
    # delete pass and fill in your code below
    im = Image.new('L',(n,n),255)
    mat = im.load()
    for x in range(n):
        for y in range(n):
            if x==0 or y==0 or x==(n-1) or y==(n-1):
             # we want or all the pixel that their 'x' value is 0 (also for 'y') and that how we are getting the top and left border
             # to get the right and down border we need the same but for (n-1) because we are counting from zero, so if the function getting number 4 so the last number in the index will be 3, and it is the fourth number (0,1,2,3)
                mat[x,y] = 0
    return im

border(8).show()

print("********************")
print("Starting the test:")

print("********************")
print("Checking for n = 3")
ans = border(3)
test = [0, 0, 0, 0, 255, 0, 0, 0, 0]
if type(ans) == Image.Image and list(ans.getdata()) == test:
    print("CORRECT: A proper border was drawn for n = 3")
else:
    print("WRONG: An improper border was drawn for n = 3")

print("********************")
print("Checking for n = 4")
ans = border(4)
test = [0, 0, 0, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0]
if type(ans) == Image.Image and list(ans.getdata()) == test:
    print("CORRECT: A proper border was drawn for n = 4")
else:
    print("WRONG: An improper border was drawn for n = 4")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")

# test qu 9
# creating a white square of 20X20 in the right bottom corner

def square(img):
    w,h = img.size
    # img_new = img.copy() --> if we want to make a copy of the given picture
    mat = img.load()
    for x in range(0,20): # we the beginning of the picture
        for y in range(h-20,h):
            mat[x,y] = 255
            # print (mat[x,y]) --> to check if the pixels are realy white
    # print (img.size)  to know the size of the picture
    return img

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking if square makes pixel in coordinate [0, 99] white for image size 100 * 100")
ans = square(Image.new('L', (100, 100), 0))

if type(ans) == Image.Image and ans.load()[0, 99] == 255:
    print("CORRECT: Pixel [0, 99] in the image is white")
else:
    print("WRONG: Pixel [0, 99] in the image is not white")

print("********************")

print("Checking if square makes pixel in coordinate [2, 95] white for image size 100 * 100")
if type(ans) == Image.Image and ans.load()[2, 95] == 255:
    print("CORRECT: Pixel [2, 95] in the image is white")
else:
    print("WRONG: Pixel [2, 95] in the image is not white")

print("********************")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")


# test qu 10
# creating black&whote picture
# black and white
# i t will work in that order:
# first we will calculate the avarge of the whole pixels values
# then if the pixel is beyond the avarge it will be colored in white,
# and if it is below the avarge it will colored in black
def black_white(img2):
    # hist = img.histogram()
    img = img2.copy()
    w, h = img.size
    mat = img.load()
    pixels_num = w * h # giving us the number of the pixels in the image (the space\area of the square)
    sum = 0
    for x in range(w):
        for y in range(h):
            sum += mat[x, y]

    avg = sum / pixels_num # sum of the pixels values with the number of pixels in the image
    for i in range(w):
        for j in range(h):
            if mat[i, j] <= avg:
                mat[i, j] = 0

            elif mat[i, j] >= avg:
                mat[i, j] = 255
 #           else:
#                mat[i, j] == 255
    return img


# without making a copy
def black_white2(img):
    w, h = img.size
    mat = img.load()
    pixels_num = w * h
    sum = 0
    for x in range(w):
        for y in range(h):
            sum += mat[x, y]

    avg = sum / pixels_num
    print(sum, pixels_num, avg)
    for i in range(w):
        for j in range(h):
            if mat[i, j] < avg:
                mat[i, j] = 0
            elif mat[i, j] > avg:
                mat[i, j] = 255
            #else:
                #mat[x,y] = 255
    return img

### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking a simple picture")
img = Image.new('L', (10, 10), 255)
mat = img.load()
for i in range(0, 5):
    for j in range(5, 10):
        mat[i, j] = i * j

ans = black_white(img)

if type(ans) == Image.Image and ans.load()[9, 0] == 255 and ans.load()[0, 9] == 0:
    print("CORRECT: Pixels [0, 9] and [9, 0] are correct")
else:
    print("WRONG: Pixels [0, 9] and [9, 0] are not correct")

print("********************")
print("Checking completely white image")
ans = black_white(Image.new('L', (10, 10), 255))

if type(ans) == Image.Image and list(ans.getdata()) == [255 for i in range(100)]:
    print("CORRECT: Image remains completely white")
else:
    print("WRONG: Image does not remain completely white")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")


# their solution for qu 10
# https://courses.campus.gov.il/courses/course-v1:TAU+ACD_TAU_cs101x+2020_1/courseware/e395874321314eabb63db32a500b3a22/9b35261357b94ee287a1a66357481d59/?child=first
# calculating tha avarage:
def get_avg(img):
    w, h = img.size
    mat = img.load()
    pixel_sum = 0
    for x in range(w):
        for y in range(h):
            pixel_sum = pixel_sum + mat[x, y]
    avg = pixel_sum / (w * h)
    return avg


# calculating the avg by histogram
# the histtogram function give us a list of 256 values (for a gray format), and in every index in the list we are give the number of pixels that are in the color of that index
# exmp: [3,1,0,2,2....] --> in the first index (o), there are 3 pixels that their value is 0 (black) and etc...
# so to claculate the sum of the wholr image we need to multiply the index by the value inside himfor example in index 3 we have 2 pixels that thier value is 3
# so to get the sum we will do 2*3=6
# and that is going on for the whole list

def get_avg_hist(img):
    hist = img.histogram()
    w, h = img.size # w*h give us the number of the pixel in the picture --> the area of a rectangle (256 is not the number of pixel but rather the number of tint)
    pixel_sum = 0
    for i in range(len(hist)):
        pixel_sum += (i*hist[i])
    avg = pixel_sum/(w*h)
    return avg


# their solution for qu 10 in the test, by calling the func' "get_avg" and not doing it in the same func'
def black_white(img):
    # Create new image
    w, h = img.size
    mat = img.load()
    img2 = img.copy()
    mat2 = img2.load()

    # Get average pixel color
    avg = get_avg(img)

    # Go over new image and change pixels according to average
    for x in range(w):
        for y in range(h):
            if mat2[x, y] < avg:
                mat2[x, y] = 0
            else:
                mat2[x, y] = 255

    return img2


def get_avg(img):
    w, h = img.size
    hist = img.histogram()
    pixel_sum = 0
    for i in range(len(hist)):
        pixel_sum = pixel_sum + (i * hist[i])
    avg = pixel_sum / (w * h)
    return avg


### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking a simple picture")
img = Image.new('L', (10, 10), 255)
mat = img.load()
for i in range(0, 5):
    for j in range(5, 10):
        mat[i, j] = i * j

ans = black_white(img)

if type(ans) == Image.Image and ans.load()[9, 0] == 255 and ans.load()[0, 9] == 0:
    print("CORRECT: Pixels [0, 9] and [9, 0] are correct")
else:
    print("WRONG: Pixels [0, 9] and [9, 0] are not correct")

print("********************")
print("Checking completely white image")
ans = black_white(Image.new('L', (10, 10), 255))

if type(ans) == Image.Image and list(ans.getdata()) == [255 for i in range(100)]:
    print("CORRECT: Image remains completely white")
else:
    print("WRONG: Image does not remain completely white")

print("********************")
print("Tests concluded, add more tests of your own below!")
print("********************")


# for more detailed explanation of nosie handling in this link:
# https: // courses.campus.gov.il / courses / course - v1: TAU + ACD_TAU_cs101x + 2020_1 / courseware / e395874321314eabb63db32a500b3a22 / de0e7645c227401db314e76ac565ac32 /?child = first
