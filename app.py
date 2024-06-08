import random

# Initialize game record
games_played = 0
games_won = 0
games_lost = 0
games_tied = 0

while True:
    # Ask the user to enter their choice
    user_choice = input("Enter your choice (rock, paper, scissors): ")

    # Verify that the user's input is valid
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter rock, paper or scissors.")
    else:
        # Generate a random choice for the computer
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("The computer chose: " + computer_choice)

        # Compare the user's choice and the computer's to determine the winner
        if user_choice == computer_choice:
            print("It's a tie.")
            games_tied += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You have won!")
            games_won += 1
        else:
            print("You have lost.")
            games_lost += 1

        games_played += 1

    # Ask the user if they want to keep playing
    play_again = input("Do you want to keep playing? (yes/no): ")
    if play_again.lower() != "yes":
        break

# Print the results
print("Games played: ", games_played)
print("Games won: ", games_won)
print("Games lost: ", games_lost)
print("Games tied: ", games_tied)