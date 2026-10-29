import random

def play_game():
    # Keep track of the score
    user_score = 0
    computer_score = 0
    
    # List of available options
    choices = ["rock", "paper", "scissors"]
    
    print("=== Welcome to Rock, Paper, Scissors ===")
    print("Type 'quit' at any time to exit the game.\n")
    
    while True:
        # Get user input and clean it up (lowercase and remove spaces)
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower().strip()
        
        # Check if the player wants to quit
        if user_choice == "quit":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break
            
        # Make sure the user typed a valid option
        if user_choice not in choices:
            print("❌ Invalid choice. Please type Rock, Paper, or Scissors.")
            continue
            
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("👔 It's a tie!")
            
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            user_score += 1
            
        else:
            print("😢 Computer wins this round!")
            computer_score += 1
            
        # Print the current score after every round
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

# Start the game
if __name__ == "__main__":
    play_game()
