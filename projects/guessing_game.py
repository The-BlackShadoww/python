# import random

# random_num = random.randint(1, 100)
# print(random_num)
# max_guess = 3
# guess_count = 0
# guessed_num = 0

# while guess_count < max_guess:
#     guessed_num = int(input("Enter a number between 1 and 100: "))
#     if guessed_num == random_num:
#         print("you win")
#         break
#     elif guessed_num > random_num:
#         guess_count += 1
#         guess_remaining = max_guess - guess_count
#         if guess_remaining == 0:
#             print("Game Over!")
#         else:
#             print("too high")
#             print(f"You have {guess_remaining} guesses left")
#     elif guessed_num < random_num:
#         guess_count += 1
#         guess_remaining = max_guess - guess_count
#         if guess_remaining == 0:
#             print("Game Over!")
#         else:
#             print("too low")
#             print(f"You have {guess_remaining} guesses left")

#! extended guessing game

import random

def get_difficulty():
    print("Choose Difficulty Level: Easy / Medium / Hard")
    while True:
        level = input("Enter difficulty: ").lower()
        if level == "easy":
            return 1, 10, 5
        elif level == "medium":
            return 1, 50, 5
        elif level == "hard":
            return 1, 100, 3
        else:
            print("Invalid choice. Please type Easy, Medium, or Hard.")

def get_valid_guess(min_val, max_val):
    while True:
        try:
            guess = int(input(f"Enter a number between {min_val} and {max_val}: "))
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"❌ Out of range. Try a number between {min_val} and {max_val}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def play_game():
    min_val, max_val, max_guess = get_difficulty()
    random_num = random.randint(min_val, max_val)
    guess_count = 0

    while guess_count < max_guess:
        guess = get_valid_guess(min_val, max_val)
        guess_count += 1

        if guess == random_num:
            print("🎉 Correct! You win!")
            break
        elif guess > random_num:
            print("📉 Too high!")
        else:
            print("📈 Too low!")

        remaining = max_guess - guess_count
        if remaining > 0:
            print(f"You have {remaining} guesses left.\n")
        else:
            print(f"💀 Game Over! The correct number was {random_num}.")

play_game()
