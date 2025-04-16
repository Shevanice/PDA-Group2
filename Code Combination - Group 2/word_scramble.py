"""
Auther: Talisa Stewart
ID: 2407311
Date: April 16, 2025
Reference:

Description: 
"""
import random

RESET = "\033[0m"
PURPLE = "\033[95m"

class NumberGuessingGame:
    def __init__(self):
        self.scores = []
        self.play_game()

    def play_game(self):
        while True:
            number_to_guess = random.randint(1, 100)
            guesses = 0
            print(PURPLE +"--------------------------------"+ RESET)
            print("Welcome to the Number Guessing Game!")
            print(PURPLE +"--------------------------------\n"+ RESET)
            print("I have picked a number between 1 and 100. Try to guess it!")

            while True:
                try:
                    guess = int(input("Enter your guess (or type '0' to quit): "))
                    if guess == 0:
                        print("Thank you for playing!")
                        self.display_scores()
                        return
                    guesses += 1
                    if guess < number_to_guess:
                        print("Higher!")
                    elif guess > number_to_guess:
                        print("Lower!")
                    else:
                        print(f"Congratulations! You've guessed the number {number_to_guess} in {guesses} tries.")
                        self.scores.append(guesses)
                        break
                except ValueError:
                    print("Please enter a valid integer.")

    def display_scores(self):
        if self.scores:
            average_score = sum(self.scores) / len(self.scores)
            best_score = min(self.scores)
            print(f"Your scores: {self.scores}")
            print(f"Average number of guesses: {average_score:.2f}")
            print(f"Best score: {best_score}")
        else:
            print("No games played.")

if __name__ == "__main__":
    NumberGuessingGame()




