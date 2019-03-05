import hangman
import guess_a_number

print("*********************************")
print("****** Choose your game! ********")
print("*********************************")

print("( 1 ) Hangman\n( 2 ) Guess a Number\n")

game = int(input("Choose a game. "))

if (game == 1):
    print("You will play Hangman.")
    hangman.play()
elif (game == 2):
    print("You will play Guess a Number.")
    guess_a_number.play()