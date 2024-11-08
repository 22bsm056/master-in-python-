import random

def play_game():
    data = {1: "snake", 2: "water", 3: "gun"}
    
    while True:
        # Prompt the user to start or stop the game
        start = int(input("Enter 1 to start the game or 0 to exit: "))
        if start == 0:
            print("Thank you for playing! Goodbye.")
            break
        elif start == 1:
            computer_choice = random.choice([1, 2, 3])
            try:
                you_choice = int(input("Enter your choice 1:snake, 2:water, 3:gun: "))
                if you_choice not in data:
                    print("Invalid choice! Please enter 1, 2, or 3.")
                    continue
                computer = data[computer_choice]
                you = data[you_choice]
                
                print(f"Your choice: {you} | Computer's choice: {computer}")

                # Determine the result
                if you == computer:
                    print("Game draw, play again.")
                elif (you == "snake" and computer == "water") or \
                     (you == "water" and computer == "gun") or \
                     (you == "gun" and computer == "snake"):
                    print("You won!")
                else:
                    print("You lost.")
                
            except ValueError:
                print("Please enter a valid integer for your choice.")
        else:
            print("Invalid input! Please enter 1 to start or 0 to exit.")

# Run the game function
play_game()
