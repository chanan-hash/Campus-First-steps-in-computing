# this code is a game I used to play in my childhood to decide who will start in all kind of game
# in hebrew it is calles "Zug o Peret"
import random

### we need to decide first what are you "even or odd"
even_odd = input("Choose your side, even\odd (enter the word even or odd): ")

computer_choice = [0,1,2,3,4,5] # acorrding to numbers you can do with one hand

count_Computer = 0
count_ME = 0

keep_playing = "true"

while keep_playing == "true":

    ComR = random.choice(computer_choice)
    # we need to change the input to an 'int' type
    print("plese Enter a number between 0-5:")
    x = input()
    x = int(x)
    my_choice = x

    if my_choice < 1 or my_choice > 5:
        print("You must chose, a number between 0-5")
        my_choice = input("plese Enter a number between 0-5:")

    else:
        # if you chose even
        if even_odd == "even":
            print("The computer choose", ComR, "and you chose", my_choice)
            if (my_choice + ComR) % 2 == 0:
                print("You win!")
                count_ME += 1
                print("win:",count_ME, "lost:",count_Computer)
            else:
                print("You lost, try again")
                count_Computer += 1
                print("win:",count_ME, "lost:",count_Computer)

       # if you chose to be odd
        elif even_odd == "odd":
            print("The computer choose", ComR, "and you chose", my_choice)

            if (my_choice + ComR) % 2 == 0:
                print("You lost, try again")
                count_Computer += 1
                print("win:", count_ME, "lost:", count_Computer)
            else:
                print("You win!!!")
                count_ME += 1
                print("win:", count_ME, "lost:", count_Computer)

