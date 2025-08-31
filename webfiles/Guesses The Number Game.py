import random
def game():
    n = random.randint(1, 100)
    guesses = 0
    a = -1
    while a != n:
        try:
            a = int(input("Guess the number (between 1 and 100): "))
            guesses += 1
            if a > n:
                print("Lower number please!")
            elif a < n:
                print("Higher number please!")
            else:
                print(f"Congratulations! You guessed the number {n} in {guesses} attempts.")
        except ValueError:
            print("Please enter a valid number.")
    return guesses
def update_hi_score():
    try:
        try:
            with open("Hi-score.txt", "r") as file:
                previous_hi_score = int(file.read().strip())
        except (FileNotFoundError, ValueError):
            previous_hi_score = float('inf')  # High score is minimal number of guesses
        while True:
            current_score = game()
            if current_score < previous_hi_score:
                print(f"New Hi-score: {current_score}! Congratulations!")
                with open("Hi-score.txt", "w") as file:
                    file.write(str(current_score))
                previous_hi_score = current_score
            else:
                print(f"Your score: {current_score}. Current Hi-score: {previous_hi_score}.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
    except Exception as e:
        print(f"An error occurred: {e}")
update_hi_score()
