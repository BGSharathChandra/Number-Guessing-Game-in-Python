# Requirements to play the Game
# Craetea a txt file in the Folder you are running the code with the name hiscore and type 100 in it. If you cant uncomment the LAST 8 LINES
# If the Code is not running in your PC then delete the Last 8 lines (27-35) and uncomment the lines from 23 to 25.

import random
randomNo = random.randint(1, 100)

guesses = 0
num = None  # Making num as None so that it does not throw error in the loop saying that num is not defined

while num != randomNo:
    guesses = guesses+1
    num = int(input("Enter the Number:"))

    if randomNo > num:
        print("Enter a Greater Number")
    elif randomNo < num:
        print("Enter a Lower Number")
    else:
        print("You Win")
        print("The Number of Guesses you have taken is ", guesses)

   # This Code in lines 24,25,26 gives you 6 turns to Guess the Number if you un comment this line even though the Code is Perfectly working then dont forget uncomment last 8 lines(27-35)
    # if guesses == 6:
       # print("You Loose ")
        # print(f"The Number the Computer had Choosen was {randomNo}")

# Reading and Printing Values
# What does the Code do from line 31 to 38?
# It will Read the Text you Have Created (hiscore) and Write the High Score in it.
print(f"You guessed the number in {guesses} guesses")



with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("You have just broken the high score by taking lesser guesses!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))