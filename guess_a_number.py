#!/usr/bin/env python

"""
Guess_a_number v.1
This is my first program (Hello world's like don't count, ok?!)
This is a classic one and allowed me to try some:

- Functions
- Loops and conditionals

"""

import random


def score_monitor(actual_score, secret_number, attempt, level):
    how_far_was_the_attempt = abs(secret_number - (attempt / level))
    actual_score = actual_score - how_far_was_the_attempt

    return actual_score


def choose_difficulty():
    selector = 0
    number_of_attempts = 0
    while (selector < 1 or selector > 3):
        print("Choose the difficulty:")
        selector_str = input("( 1 ) EASY\n( 2 ) MEDIUM\n( 3 ) HARD\n")
        selector = int(selector_str)

        if selector == 1:
            number_of_attempts = 20
        elif selector == 2:
            number_of_attempts = 10
        elif selector == 3:
            number_of_attempts = 5
        else:
            print("Invalid option\n\n")

    return number_of_attempts, selector

def play():
    print("*********************")
    print("** Guess a Number! **")
    print("*********************")

    inferior_limit = 1
    superior_limit = 100
    actual_score = 1000

    # ================================================================================
    def get_number(inferior_limit, superior_limit):
        # Tests whether the number is within the allowed range
        player_attempt = 0
        number_below = True
        number_above = True

        while (number_below or number_above):
            player_attempt_str = input("Type a number\n")
            print(f"You have typed...{player_attempt_str}\n")
            player_attempt = int(player_attempt_str)

            if (number_below or number_above):
                print(f"Only tries between {inferior_limit} and {superior_limit} are allowed.\nPlease, try again.\n")

            number_below = player_attempt < inferior_limit
            number_above = player_attempt > superior_limit
        return player_attempt

    def generate_secret_number(inferior_limit, superior_limit):
        return round(random.randrange(inferior_limit, superior_limit + 1))


    secret_number = generate_secret_number(inferior_limit, superior_limit)
    number_of_attempts, level = choose_difficulty()

    for actual_round in range(1, number_of_attempts + 1):
        print(f"Your score was: {actual_score}")
        print(f"Attempt {actual_round} of {number_of_attempts}")

        attempt = get_number(inferior_limit, superior_limit)

        hit = secret_number == attempt
        greater = attempt > secret_number
        lesser = attempt < secret_number

        if (hit):
            print("You hit! Congratulation!\n")
            print(f"Your final score was {actual_score}\n")
            break
        else:
            if (greater):
                print("\n\nWrong choise!\n TIP --> Your attempt was ABOVE of secret number.\n")
            elif (lesser):
                print("\n\nWrong choise!\n TIP --> Your attempt was BELOW of secret number.\n")
        actual_score = score_monitor(actual_score, secret_number, attempt, level)

if(__name__ == "__main__"):
    play()
