import random
print("--------------- Welcome to my guessing number game! ----------------")
print("--------------- Good luck and have fun! ----------------")
def guessingNumber():
    score = 100
    newListOfNumbers = []
    print("Start range is from 0 to your choice")
    newRange = int(input("Choose range of number to guess: "))
    for i in range(0, newRange):
        newListOfNumbers.append(i)
    chooseTheNumberForPlayer = int(random.choice(newListOfNumbers))
    print("#-------------------------------- Your range is between 0 and", newRange, "---------------------#")
    playerNumber = int(input("Choose your number between above range: "))
    while chooseTheNumberForPlayer != playerNumber and (score > 0):
        if playerNumber < chooseTheNumberForPlayer:
            if (chooseTheNumberForPlayer % 2 == 0):
                print("Your number is lower than the given number which can divisible by 2")
                if (newRange >= 50):
                    helpPlayer1 = []
                    for i in range(0, int(chooseTheNumberForPlayer)):
                        if (i % 2 == 0):
                            helpPlayer1.append(i)
                    print("Try these numbers:", helpPlayer1, "if doesn't works try plus 2 to highest number on this list")
                else:
                    print("You can do it :D")
            elif (chooseTheNumberForPlayer %3 == 0):
                print("Your number is lower than the given number which can divisible by 3")
                if (newRange >= 50):
                    helpPlayer2 = []
                    for i in range(0, int(chooseTheNumberForPlayer)):
                        if (i % 2 == 0):
                            helpPlayer2.append(i)
                    print("Try these numbers:", helpPlayer2, "if doesn't works try plus 2 to highest number on this list")
                else:
                    print("You can do it :D")
            else:
                print("Your number is lower than the given number either divisible by 3 nor 2")
                if (newRange >= 50):
                    helpPlayer3 = []
                    for i in range(playerNumber, chooseTheNumberForPlayer):
                        if (i % 2 != 0) and (i % 3 != 0):
                            helpPlayer3.append(i)
                    helpPlayer3.append(chooseTheNumberForPlayer)
                    print("Try these numbers", helpPlayer3)
                else:
                    print("You can do it :D")
            score = score - random.randint(15,20)

            playerNumber = int(input("Nice guess, but not enough, try again: "))
        
        else:
            if (chooseTheNumberForPlayer % 2 == 0):
                print("Your number is higher than the given number which can divisible by 2")
                if (newRange >= 50):
                    helpPlayer4 = []
                    for i in range(0, int(chooseTheNumberForPlayer)):
                        if (i % 2 == 0):
                            helpPlayer4.append(i)
                    print("Try these numbers:", helpPlayer4, "if doesn't works try plus 2 to highest number on this list")
                else:
                    print("You can do it :D")
            elif (chooseTheNumberForPlayer % 3 == 0):
                print("Your number is higher than the given number which can divisible by 3")
                if (newRange >= 50):
                    helpPlayer5 = []
                    for i in range(0, int(chooseTheNumberForPlayer)):
                        if (i % 3 == 0):
                            helpPlayer5.append(i)
                    print("Try these numbers:", helpPlayer5, "if doesn't works try plus 3 to highest number on this list")
                else:
                    print("You can do it :D")

            else:
                print("Your number is higher than the given number either divisible by 3 nor 2")
                if (newRange >= 50):
                    helpPlayer6 = []
                    for i in range(playerNumber, chooseTheNumberForPlayer):
                        if (i % 2 != 0) and (i % 3 != 0):
                            helpPlayer6.append(i)
                        helpPlayer6.append(chooseTheNumberForPlayer)
                    print("Try these numbers", helpPlayer6)
                else:
                    print("You can do it :D")
            score = score - random.randint(15,20)
            playerNumber = int(input("Nice guess, but not enough, try again: "))
    else:
        if score > 0:
            print("Congratulations, you have done the game!")
            print("Here is your score:", score)
        else:
            print("You are out of score, better luck next time")
        input("Press any key to end")

guessingNumber()