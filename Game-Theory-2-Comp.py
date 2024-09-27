import random  # Import the random module for generating random choices
import csv  # Import the CSV module to write data to CSV files
import os  # Import the OS module for interacting with the file system
import pandas as pd  # Import pandas for data manipulation and saving to Excel files

# Function to export game data to both CSV and Excel files
# data_list: the list containing all game rounds with player scores
def excel(data_list):
    # Set the file path for the CSV file
    csv_file_path = "output.csv"
    # Get the absolute path of the CSV file
    csv_file_path_absolute = os.path.join(os.getcwd(), csv_file_path)

    # Write the data to a CSV file
    with open(csv_file_path_absolute, "w", newline="") as csvfile:
        csv.writer(csvfile).writerows(data_list)  # Write rows of data from the list to the CSV file
    print("CSV file saved at:", csv_file_path_absolute)  # Notify the user of the CSV file location

    # Convert the data list to a pandas DataFrame for exporting to Excel
    df = pd.DataFrame(data_list)
    # Set the file path for the Excel file
    excel_file_path = "data-1.xlsx"
    # Write the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)
    print(f"Excel file created at: {excel_file_path}")  # Notify the user of the Excel file location

    # Read back the data from the Excel file to verify the content
    dx = pd.read_excel(excel_file_path)
    print(dx)  # Print the data from the Excel file for verification

# Function to add the data from each game round to the list
# data_list: list storing results of each round
# n_round: the current round number
# player1_score: player 1's cumulative score
# player2_score: player 2's cumulative score
def add_data(data_list, n_round, player1_score, player2_score):
    rounds = n_round  # Store the current round number
    p1 = player1_score  # Store player 1's score
    p2 = player2_score  # Store player 2's score

    # Append a dictionary with round number and player scores to the data list
    data_list.append({"Round": rounds, "Player 1 Score": p1, "Player 2 Score": p2})

# Commented out function to display the data (can be used for debugging)
# def display_data(data_list):
#    print("\nData:")
#    for entry in data_list:
#        print(entry)

# Function to calculate the outcome of a Prisoner's Dilemma round
# player1_choice: "cooperate" or "betray" - Player 1's choice for the round
# player2_choice: "cooperate" or "betray" - Player 2's choice for the round
# Returns: (player1_reward, player2_reward) based on their choices
def prisoner_dilemma(player1_choice, player2_choice):
    # Define rewards based on the classic Prisoner's Dilemma payoff matrix
    betrayal_reward = 5        # Reward for both betraying
    cooperation_reward = 3     # Reward for both cooperating
    temptation_reward = 8      # Temptation reward for betraying while the other cooperates
    punishment_reward = 1      # Punishment for mutual betrayal

    # If both players betray each other
    if player1_choice == "betray" and player2_choice == "betray":
        return punishment_reward, punishment_reward  # Both get the punishment reward

    # If both players cooperate
    elif player1_choice == "cooperate" and player2_choice == "cooperate":
        return cooperation_reward, cooperation_reward  # Both get the cooperation reward

    # If player 1 betrays and player 2 cooperates
    elif player1_choice == "betray" and player2_choice == "cooperate":
        return temptation_reward, 0  # Player 1 gets the temptation reward, player 2 gets 0

    # If player 1 cooperates and player 2 betrays
    elif player1_choice == "cooperate" and player2_choice == "betray":
        return 0, temptation_reward  # Player 1 gets 0, player 2 gets the temptation reward

# Different computer strategies for choosing between cooperation and betrayal

# Random strategy: randomly choose between cooperation or betrayal
# x: opponent's last choice (not used here)
# Returns: "cooperate" or "betray" randomly
def computer_strategy_random(x):
    y = random.choice([0, 1])  # Randomly select 0 (cooperate) or 1 (betray)
    if y == 0:
        return "cooperate"
    else:
        return "betray"

# Always betray strategy: always choose betrayal
# x: opponent's last choice (not used here)
# Returns: "betray"
def computer_strategy_always_betray(x):
    return "betray"  # Always return "betray"

# Always cooperate strategy: always choose cooperation
# x: opponent's last choice (not used here)
# Returns: "cooperate"
def computer_strategy_always_cooperate(x):
    return "cooperate"  # Always return "cooperate"

# Tit-for-tat strategy: do whatever the opponent did in the last round
# x: opponent's last choice
# Returns: opponent's last action (cooperate or betray)
def computer_strategy_tit_for_tat(x):
    return x  # Mimic the opponent's last action

# Strategy C: 50% chance to mimic opponent's last action, 50% chance to betray
# x: opponent's last choice
# Returns: "cooperate" or "betray"
def computer_strategy_C(x):
    y = random.choice([0, 1])  # Randomly choose between mimic or betrayal
    if y == 1:
        return x  # Mimic opponent's last action
    else:
        return "betray"  # Otherwise, betray

# Strategy D: 50% chance to mimic opponent's last action, 50% chance to cooperate
# x: opponent's last choice
# Returns: "cooperate" or "betray"
def computer_strategy_D(x):
    y = random.choice([0, 1])  # Randomly choose between mimic or cooperation
    if y == 1:
        return x  # Mimic opponent's last action
    else:
        return "cooperate"  # Otherwise, cooperate

# Strategy Xb: biased towards betrayal with 70% chance
# x: opponent's last choice (not used here)
# Returns: "cooperate" or "betray" with a bias towards betrayal
def computer_stratergy_Xb(x):
    bias = 0.7  # 70% chance to betray
    y = random.random()  # Generate a random float between 0 and 1
    if y < bias:
        return "betray"
    else:
        return "cooperate"

# Strategy Xc: biased towards cooperation with 70% chance
# x: opponent's last choice (not used here)
# Returns: "cooperate" or "betray" with a bias towards cooperation
def computer_stratergy_Xc(x):
    bias = 0.7  # 70% chance to cooperate
    y = random.random()  # Generate a random float between 0 and 1
    if y < bias:
        return "cooperate"
    else:
        return "betray"

# Main function to run the game
def main():
    data_list = []  # Initialize an empty list to store game data (rounds and scores)
    rounds = int(input("Enter the number of rounds: "))  # Get the number of rounds to play

    # Define the available strategies for the computers
    strategies = [
        computer_strategy_random,
        computer_strategy_always_betray,
        computer_strategy_always_cooperate,
        computer_strategy_tit_for_tat,
        computer_strategy_C,
        computer_strategy_D,
        computer_stratergy_Xb,
        computer_stratergy_Xc,
    ]

    # Ask the user to select a strategy for each computer
    print("Choose computer strategy:")
    for i, strategy in enumerate(strategies):
        print(f"{i + 1}. {strategy.__name__}")  # Display the strategy options

    # Select the first computer's strategy
    computer_strategy_choice1 = int(input("Enter the number for computer strategy 1: ")) - 1
    computer_strategy1 = strategies[computer_strategy_choice1]

    # Select the second computer's strategy
    computer_strategy_choice2 = int(input("Enter the number for computer strategy 2: ")) - 1
    computer_strategy2 = strategies[computer_strategy_choice2]

    # Initialize the scores for both computers
    player1_score = 0
    player2_score = 0
    computer_choice1 = "cooperate"  # Initialize the first computer's choice to cooperate
    computer_choice2 = "cooperate"  # Initialize the second computer's choice to cooperate

    # Main game loop, iterating over the number of rounds
    for round_num in range(1, rounds + 1):
        # print(f"\nRound {round_num}:")  # Uncomment to print the round number if needed

        # Determine each computer's choice based on the selected strategies
        computer_choice1 = computer_strategy1(computer_choice2)
        computer_choice2 = computer_strategy2(computer_choice1)

        # Calculate rewards for each computer based on their choices
        reward_player1, reward_player2 = prisoner_dilemma(computer_choice2, computer_choice1)

        # Update the cumulative scores for both computers
        player1_score = reward_player1 + player1_score
        player2_score = reward_player2 + player2_score

        # Add the data for this round to the data list
        add_data(data_list, round_num, player1_score, player2_score)

    # After all rounds, print the final scores
    print("\nGame Over!")
    print(f"Computer 1 Score: {player1_score}\tComputer 2 Score: {player2_score}")

    # Export the game data to both CSV and Excel files
    excel(data_list)

# Boilerplate to ensure the script runs only when executed directly (not when imported)
if __name__ == "__main__":
    main()  # Call the main function to start the game

