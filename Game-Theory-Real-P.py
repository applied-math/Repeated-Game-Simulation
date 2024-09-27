# Function to add data from each round into a list for storage
# data_list: the list storing results of each round
# n_round: the current round number
# player1_score: the cumulative score for player 1
# player2_score: the cumulative score for player 2
def add_data(data_list, n_round, player1_score, player2_score):
    # Assign the current round and player scores to variables
    rounds = n_round
    p1 = player1_score  # Player 1's current score
    p2 = player2_score  # Player 2's current score

    # Append a dictionary containing the round number and both player scores to the data list
    data_list.append({"Round": rounds, "Player 1 Score": p1, "Player 2 Score": p2})


# Function to display all the round data after the game is over
# data_list: the list containing all round data (round number, player scores)
def display_data(data_list):
    print("\nData:")  # Print a header for the data display
    # Iterate over the data list, where each entry represents one round of data
    for entry in data_list:
        # Print the dictionary entry for each round, which contains round number and player scores
        print(entry)


# Function to simulate the prisoner's dilemma game between two players
# player1_choice: "cooperate" or "betray" - Player 1's choice in the current round
# player2_choice: "cooperate" or "betray" - Player 2's choice in the current round
# Returns: tuple of (player1_reward, player2_reward) based on their choices
def prisoner_dilemma(player1_choice, player2_choice):
    # Define the reward system based on game theory:
    betrayal_reward = 5  # Reward when both players betray
    cooperation_reward = 3  # Reward when both players cooperate
    temptation_reward = 8  # Reward for the betrayer if the opponent cooperates
    punishment_reward = 1  # Punishment for both if both betray

    # Case where both players choose to betray each other
    if player1_choice == "betray" and player2_choice == "betray":
        return (
            punishment_reward,
            punishment_reward,
        )  # Both receive the punishment reward

    # Case where both players choose to cooperate
    elif player1_choice == "cooperate" and player2_choice == "cooperate":
        return (
            cooperation_reward,
            cooperation_reward,
        )  # Both receive the cooperation reward

    # Case where player 1 betrays and player 2 cooperates
    elif player1_choice == "betray" and player2_choice == "cooperate":
        return (
            temptation_reward,
            0,
        )  # Player 1 gets the temptation reward, player 2 gets nothing

    # Case where player 1 cooperates and player 2 betrays
    elif player1_choice == "cooperate" and player2_choice == "betray":
        return (
            0,
            temptation_reward,
        )  # Player 1 gets nothing, player 2 gets the temptation reward


# Main function to handle the overall flow of the game
# n_rounds: the total number of rounds to play
def main(n_rounds):
    # Initialize an empty list to store the data from all rounds
    data_list = []

    # Initialize the scores for both players
    player1_score = 0
    player2_score = 0

    # Game loop that runs for the specified number of rounds
    for n_round in range(
        1, n_rounds + 1
    ):  # Loop through rounds starting from 1 to n_rounds
        print(f"Rounds {n_round}")  # Print the current round number

        # Player 1's choice: input either 'cooperate' or 'betray'
        player1_choice = input("Player 1, choose 'cooperate' or 'betray': ").lower()

        # Player 2's choice: input either 'cooperate' or 'betray'
        player2_choice = input("Player 2, choose 'cooperate' or 'betray': ").lower()

        # Input validation: Ensure both player choices are valid ('cooperate' or 'betray')
        if player1_choice not in ["cooperate", "betray"] or player2_choice not in [
            "cooperate",
            "betray",
        ]:
            # If invalid choices are entered, display an error and end the game
            print("Invalid choices. Please enter 'cooperate' or 'betray'.")
            return  # End the function early due to invalid input

        # Calculate the rewards for both players based on their choices using the prisoner_dilemma function
        player1_reward, player2_reward = prisoner_dilemma(
            player1_choice, player2_choice
        )

        # Display the choices and rewards for both players for this round
        print(f"\nResults:")
        print(
            f"Player 1's choice: {player1_choice}\tPlayer 2's choice: {player2_choice}"
        )
        print(
            f"Player 1's reward: {player1_reward}\tPlayer 2's reward: {player2_reward}"
        )

        # Update the cumulative scores for both players by adding the rewards from the current round
        player1_score = player1_score + player1_reward
        player2_score = player2_score + player2_reward

        # Display the updated cumulative scores for both players after this round
        print(f"Player 1 Score: {player1_score}\tPlayer 2 Score: {player2_score}\n")

        # Add the data for this round to the data list using the add_data function
        add_data(data_list, n_round, player1_score, player2_score)

    # After all rounds are completed, print "Game Over!" and display the final scores
    print("Game Over!")
    print("Final Scores:")
    print(f"Player 1: {player1_score}\tPlayer 2: {player2_score}")

    # Display all the round data collected in the data list using the display_data function
    display_data(data_list)


# This section prompts the user for the number of rounds and starts the game
# Input: User enters the number of rounds to play
num_rounds = int(input("Enter the number of rounds: "))

# Call the main function to start the game with the input number of rounds
main(num_rounds)
