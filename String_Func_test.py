str = "hello, world!"
COMMA = ", "
print(str.split(COMMA)[0])
# split without anything creates list with the word themself of the string
# if we put a index we will get the word itself no in a list - very important to notice
# because this is a difference between string and list format, we are asking/getting the objectqword inside the index itself
# when split getting an object inside it it split the string acorrding to the object

str11 = "Hello, my name is Chanan"
print(str11.split())
# ['Hello,', 'my', 'name', 'is', 'Chanan']
print(str11.split()[2])
# name
print(str11.split(COMMA))
# ['Hello', 'my name is Chanan']
print(str11.split(COMMA)[1])
# my name is Chanan

str12 = "Hi, how are you? isn't that a lovely day?"
# lets put now bunch of commas to see how it will split it
str13 = "Hi, how are you, isn't that, a lovely day?"
print(str13.split(COMMA))
# ['Hi', 'how are you', "isn't that", 'a lovely day?']
# Every object in the list is acorrding to were is the comma (",")

# remove and replace
str14 = "hello every one, how are you"
# it replace all the places with the first char with the second
print(str14.replace("e","a"))
# if we want to remove a char, we can replace it with empty string("")
print(str14.replace("e",""))
# if we put a number it replace the char the as much as the number we have put
print(str14.replace("e","",1))
# here it will replace "e" with "a" only once

print()
# join


