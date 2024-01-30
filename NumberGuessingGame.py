import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("To Win the game you need to correctly guess the number from the range you have provided")
    
    lower_bound = int(input("Enter the Minimum value of the range: "))
    upper_bound = int(input("Enter the Maximum value of the range: "))
    
    target_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    guess = None
    
    while guess != target_number:
        guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        attempts += 1

        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly!")
            print(f"It took you {attempts} attempts.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()
    else:
        print("Thank you for playing!")


number_guessing_game()
