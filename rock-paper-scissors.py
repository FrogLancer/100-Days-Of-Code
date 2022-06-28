#  Day 4, Rock-Paper-Scissors


import random

playing = True


def playAgain():
    '''Asks the user if they want to play again and returns True or False depending on the user's choice.'''
    userPlayChoice = input('Play again?(y/n) ').lower()
    while userPlayChoice != 'y' or userPlayChoice != 'n':
        if userPlayChoice == 'y':
            return True
        elif userPlayChoice == 'n':
            return False
        else:
            userPlayChoice = input("Please enter 'y' or 'n'.").lower()


while playing == True:
    cpuChoice = str(random.randint(1, 3))

    playerChoice = input("""Choose rock, paper, or scissors: """).lower()

    if cpuChoice == '1':  # cpu chose rock
        if playerChoice == 'rock':  # user chose rock
            print("The computer chose rock. It's a draw.")
            playing = playAgain()

        if playerChoice == 'scissors':  # user chose scissors
            print("The computer chose rock, you lose.")
            playing = playAgain()

        if playerChoice == 'paper':  # user chose paper
            print("The computer chose rock. You win!")
            playing = playAgain()

    elif cpuChoice == '2':  # cpu chose paper
        if playerChoice == 'rock':  # user chose rock
            print("The computer chose paper. You lose")
            playing = playAgain()

        if playerChoice == 'paper':  # user chose paper
            print("The computer chose paper. It's a draw.")
            playing = playAgain()

        if playerChoice == 'scissors':  # user chose scissors
            print("The computer chose paper. You win!")
            playing = playAgain()

    elif cpuChoice == '3':  # cpu chose scissors
        if playerChoice == 'rock':  # user chose rock
            print("The computer chose scissors. You win!")
            playing = playAgain()

        if playerChoice == 'paper':  # user chose paper
            print("The computer chose scissors. You lose")
            playing = playAgain()

        if playerChoice == 'scissors':  # user chose scissors
            print("The computer chose scissors. It's a draw.")
            playing = playAgain()
