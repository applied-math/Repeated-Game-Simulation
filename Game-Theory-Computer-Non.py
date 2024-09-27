import random  # Import the random module for generating random choices


# Function to add data for each round into a list
# data_list: the list storing the results of each round
# n_round: the round number
# player1_score: the score of player 1 (human player)
# player2_score: the score of player 2 (computer)
def add_data(data_list, n_round, player1_score, player2_score):
    rounds = n_round  # Assign the current round number
    p1 = player1_score  # Assign player 1's (human) score
    p2 = player2_score  # Assign player 2's (computer) score
    # Append the round number and the scores of both players to the data list as a dictionary
    data_list.append({"Round": rounds, "Player 1 Score": p1, "Player 2 Score": p2})


# Function to display all data after the game is over
# data_list: the list containing all the game data (rounds, player scores)
def display_data(data_list):
    print("\nData:")  # Print header for data display
    # Loop over each entry (round data) in data_list
    for entry in data_list:
        print(
            entry
        )  # Print the dictionary containing round data (round number, player scores)


# Function to simulate the prisoner's dilemma game between two players
# player1_choice: the choice of player 1 ("cooperate" or "betray")
# player2_choice: the choice of player 2 ("cooperate" or "betray")
# Returns the rewards for both players based on their choices
def prisoner_dilemma(player1_choice, player2_choice):
    # Define the reward values based on game theory:
    betrayal_reward = 5  # Reward if both betray
    cooperation_reward = 3  # Reward if both cooperate
    temptation_reward = 8  # Reward for the betrayer if the other player cooperates
    punishment_reward = 1  # Punishment if both betray

    # Condition where both players choose to betray
    if player1_choice == "betray" and player2_choice == "betray":
        return punishment_reward, punishment_reward  # Both get the punishment reward
    # Condition where both players choose to cooperate
    elif player1_choice == "cooperate" and player2_choice == "cooperate":
        return cooperation_reward, cooperation_reward  # Both get the cooperation reward
    # Condition where player 1 betrays and player 2 cooperates
    elif player1_choice == "betray" and player2_choice == "cooperate":
        return temptation_reward, 0  # Player 1 gets temptation reward, Player 2 gets 0
    # Condition where player 1 cooperates and player 2 betrays
    elif player1_choice == "cooperate" and player2_choice == "betray":
        return 0, temptation_reward  # Player 1 gets 0, Player 2 gets temptation reward
    else:
        # Handle invalid choices by returning 0 rewards
        print("Invalid choices encountered in prisoner_dilemma.")
        return 0, 0


# Computer strategy function that picks a random choice between "cooperate" and "betray"
# Returns: "cooperate" or "betray" randomly
def computer_strategy_random():
    return random.choice(
        ["cooperate", "betray"]
    )  # Randomly return one of the two options


# Computer strategy function where the computer always chooses "betray"
# Returns: "betray"
def computer_strategy_always_betray():
    return "betray"  # Always return "betray"


# Computer strategy function where the computer always chooses "cooperate"
# Returns: "cooperate"
def computer_strategy_always_cooperate():
    return "cooperate"  # Always return "cooperate"


# Main function that handles the overall flow of the game
def main():
    data_list = []  # Initialize an empty list to store game data (rounds and scores)

    # Input: Number of rounds to play
    while True:
        try:
            rounds = int(input("Enter the number of rounds: "))
            if rounds <= 0:
                print("Please enter a positive integer for the number of rounds.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of rounds.")

    # Define the available computer strategies
    strategies = [
        computer_strategy_random,  # Random strategy
        computer_strategy_always_betray,  # Always betray strategy
        computer_strategy_always_cooperate,  # Always cooperate strategy
    ]

    # Print available computer strategies and let the user choose one
    print("\nChoose computer strategy:")
    for i, strategy in enumerate(strategies):
        print(f"{i + 1}. {strategy.__name__}")  # Print the strategy names

    # Input: Choose a computer strategy from the list (user input is 1-based index)
    while True:
        try:
            computer_strategy_choice = (
                int(input("Enter the number for computer strategy: ")) - 1
            )
            if 0 <= computer_strategy_choice < len(strategies):
                break
            else:
                print(f"Please enter a number between 1 and {len(strategies)}.")
        except ValueError:
            print(
                "Invalid input. Please enter a valid number corresponding to the strategies."
            )

    computer_strategy = strategies[
        computer_strategy_choice
    ]  # Select the chosen strategy

    # Initialize the scores for player 1 (human) and the computer (player 2)
    player1_score = 0
    player2_score = 0

    # Main game loop, iterating over the number of rounds
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")  # Print the current round number

        # Input: Player 1 (human) chooses either "cooperate" or "betray"
        while True:
            player1_input = input(
                "Your choice (1 for cooperate / 2 for betray): "
            ).strip()
            if player1_input == "1":
                player1_choice = "cooperate"
                break
            elif player1_input == "2":
                player1_choice = "betray"
                break
            else:
                print("Invalid input. Please enter '1' to cooperate or '2' to betray.")

        # Computer chooses its action based on the selected strategy
        computer_choice = computer_strategy()

        # Display the computer's choice
        print(f"Computer's choice: {computer_choice}")

        # Get the rewards for both players based on their choices
        reward_player1, reward_player2 = prisoner_dilemma(
            player1_choice, computer_choice
        )

        # Update player 1's (human) and computer's (player 2) total scores by adding the rewards from the current round
        player1_score += reward_player1
        player2_score += reward_player2

        # Display the updated scores after each round
        print(f"Your Score: {player1_score}\tComputer's Score: {player2_score}")

        # Add the data for the current round to the data list
        add_data(data_list, round_num, player1_score, player2_score)

    # Game over section
    print("\nGame Over!")  # Notify that the game is over
    print("Final Scores:")  # Display the final scores
    print(f"Your Score: {player1_score}\tComputer's Score: {player2_score}")

    # Display all the game data (rounds, scores, etc.)
    display_data(data_list)


# Boilerplate to ensure the script runs only when executed directly (not when imported)
if __name__ == "__main__":
    main()  # Call the main function to start the game
