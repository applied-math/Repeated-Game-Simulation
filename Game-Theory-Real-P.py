def add_data(data_list, n_round, player1_score, player2_score):
    rounds = n_round
    p1 = player1_score
    p2 = player2_score
    data_list.append({"Round": rounds, "Player 1 Score": p1, "Player 2 Score": p2})


def display_data(data_list):
    print("\nData:")
    for entry in data_list:
        print(entry)


def prisoner_dilemma(player1_choice, player2_choice):
    betrayal_reward = 5
    cooperation_reward = 3
    temptation_reward = 8
    punishment_reward = 1

    if player1_choice == "betray" and player2_choice == "betray":
        return punishment_reward, punishment_reward
    elif player1_choice == "cooperate" and player2_choice == "cooperate":
        return cooperation_reward, cooperation_reward
    elif player1_choice == "betray" and player2_choice == "cooperate":
        return temptation_reward, 0
    elif player1_choice == "cooperate" and player2_choice == "betray":
        return 0, temptation_reward


def main(n_rounds):
    data_list = []
    player1_score = 0
    player2_score = 0
    for n_round in range(1, n_rounds + 1):
        print(f"Rounds {n_round}")
        player1_choice = input("Player 1, choose 'cooperate' or 'betray': ").lower()
        player2_choice = input("Player 2, choose 'cooperate' or 'betray': ").lower()
        if player1_choice not in ["cooperate", "betray"] or player2_choice not in [
            "cooperate",
            "betray",
        ]:
            print("Invalid choices. Please enter 'cooperate' or 'betray'.")
            return
        player1_reward, player2_reward = prisoner_dilemma(
            player1_choice, player2_choice
        )
        print(f"\nResults:")
        print(
            f"Player 1's choice: {player1_choice}\tPlayer 2's choice: {player2_choice}"
        )
        print(
            f"Player 1's reward: {player1_reward}\tPlayer 2's reward: {player2_reward}"
        )
        player1_score = player1_score + player1_reward
        player2_score = player2_score + player2_reward
        print(f"Player 1 Score: {player1_score}\tPlayer 2 Score: {player2_score}\n")
        add_data(data_list, n_round, player1_score, player2_score)
    print("Game Over!")
    print("Final Scores:")
    print(f"Player 1: {player1_score}\tPlayer 2: {player2_score}")
    display_data(data_list)


num_rounds = int(input("Enter the number of rounds: "))
main(num_rounds)
