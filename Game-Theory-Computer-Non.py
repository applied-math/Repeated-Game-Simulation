import random

def add_data(data_list, n_round, player1_score, player2_score):
    rounds = n_round
    p1 = player1_score
    p2 = player2_score
    data_list.append({"Round" : rounds, "Player 1 Score" : p1, "Player 2 Score" : p2})

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

def computer_strategy_random():
    return random.choice(["cooperate", "betray"])

def computer_strategy_always_betray():
    return "betray"

def computer_strategy_always_cooperate():
    return "cooperate"

def main():
    data_list = []
    rounds = int(input("Enter the number of rounds: "))

    strategies = [
        computer_strategy_random,
        computer_strategy_always_betray,
        computer_strategy_always_cooperate
    ]
    print("Choose computer strategy:")
    for i, strategy in enumerate(strategies):
        print(f"{i + 1}. {strategy.__name__}")

    computer_strategy_choice = int(input("Enter the number for computer strategy: "))
    computer_strategy = strategies[computer_strategy_choice]

    player1_score = 0
    player2_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")

        player1_choice = input("Your choice (cooperate/betray): ")
        computer_choice = computer_strategy()

        print(f"Computer's choice: {computer_choice}")

        reward_player1, reward_player2 = prisoner_dilemma(player1_choice, computer_choice)

        player1_score += reward_player1
        player2_score += reward_player2

        print(f"Your Score: {player1_score}\tComputer's Score: {player2_score}")
        add_data(data_list, round_num, player1_score, player2_score)
    print("\nGame Over!")
    print("Final Scores:")
    print(f"Your Score: {player1_score}\tComputer's Score: {player2_score}")
    display_data(data_list)
if __name__ == "__main__":
    main()
