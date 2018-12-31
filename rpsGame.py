import random
print("ROCK - PAPER - SCISSORS GAME")
list = ["rock","paper","scissors"]
again = True


while again:
    y = input("Please enter your choice(Rock, Scissors, Paper) : ")  # Players answer

    x = random.choice(list)  # Computers Answer

    if x == y:
        print("Computer chose " + x.upper() + " you chose " + y.upper() + " so it's a tie you will get to choose again.")
        continue
    elif y == "rock":
        if x == "paper":
            print("Computer chose " + x.upper() + " you chose " + y.upper() + " so COMPUTER won.")
        else:
            print("Computer chose " + x.upper() + " you chose " + y.upper() + " so YOU won.")


    elif y == "paper":
        if x == "rock":
            print("Computer chose " + x.upper() + " you chose " + y.upper() + " so YOU won.")

        else:
            print("Computer chose " + x.upper() + " you chose " + y.upper() + " so COMPUTER won.")


    elif y == "scissors":
        if x == "rock":
            print("Computer chose " + x.upper() + " you chose " + y.upper() + " so COMPUTER won.")

        else:
            print("Computer chose " + x.upper() + " you chose " + y.upper() + " so YOU won.")
    play = input("Do you want to play again? >  ")

    if play == "no":
        again = False





