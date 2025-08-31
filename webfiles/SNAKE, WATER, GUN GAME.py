import random
def game():
    choices = ["Snake", "Water", "Gun"]
    player_choice = input("Enter 'Snake', 'Water', or 'Gun': ").capitalize()
    while player_choice not in choices:
        print("Invalid choice! Please choose 'Snake', 'Water', or 'Gun'.")
        player_choice = input("Enter 'Snake', 'Water', or 'Gun': ").capitalize()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a draw!")
        return 0  
    elif (player_choice == "Snake" and computer_choice == "Water") or \
         (player_choice == "Water" and computer_choice == "Gun") or \
         (player_choice == "Gun" and computer_choice == "Snake"):
        print("You win!")
        return 1  
    else:
        print("You lose!")
        return -1  

def update_hi_score():
    try:
        try:
            with open("I:\Study\Golu lession\C lanuge\Hi-score Snake,Water,Gun Game.txt", "r") as file:
                previous_hi_score = int(file.read().strip()) 
        except (FileNotFoundError, ValueError):
            previous_hi_score = 0
        current_score = 0
        while True:
            current_score += game()  
            if current_score > previous_hi_score:
                print(f"New Hi-score: {current_score}! Congratulations!")
                with open("Hi-score Snake,Water,Gun Game.txt", "w") as file:
                    file.write(str(current_score))
                break
            else:
                print(f"Your score: {current_score}. Current Hi-score: {previous_hi_score}.")
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again != "yes":
                    break
    except Exception as e:
        print(f"An error occurred: {e}")
update_hi_score()

