import random
import csv
import os
import pandas as pd

def excel(data_list):
    csv_file_path = "output.csv"
    csv_file_path_absolute = os.path.join(os.getcwd(), csv_file_path)
    with open(csv_file_path_absolute, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data_list)
    print("CSV file saved at:", csv_file_path_absolute)
    df = pd.DataFrame(data_list)
    excel_file_path = "data-1.xlsx"
    df.to_excel(excel_file_path, index=False)
    print(f'Excel file created at: {excel_file_path}')
    dx = pd.read_excel(excel_file_path)
    print(dx)


def add_data(data_list, n_round, player1_score, player2_score):
    rounds = n_round
    p1 = player1_score
    p2 = player2_score
    data_list.append({"Round" : rounds, "Player 1 Score" : p1, "Player 2 Score" : p2})
    
#def display_data(data_list):
#    print("\nData:")
#    for entry in data_list:
#        print(entry)

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

def computer_strategy_random(x):
    y = random.choice([0,1])
    if y == 0:
        return "cooperate"
    else:
        return "betray"
def computer_strategy_always_betray(x):
    return "betray"
def computer_strategy_always_cooperate(x):
    return "cooperate"
def computer_strategy_tit_for_tat(x):
    return x
def computer_strategy_C(x):
    y = False
    y = random.choice([True,False])
    if y == True:
        return x
    else:
        return "betray"
def computer_strategy_D(x):
    y = False
    y = random.choice([True,False])
    if y == True:
        return x
    else:
        return "Cooperate"
def computer_stratergy_Xb(x):
    bias = 0.7
    y = random.random()
    if y < bias:
        return "betray"
    else:
        return "cooperate"
def computer_stratergy_Xc(x):
    bias = 0.7
    y = random.random()
    if y < bias:
        return "cooperate"
    else:
        return "betray"
def main():
    data_list = []
    rounds = int(input("Enter the number of rounds: "))
    strategies = [
        computer_strategy_random,
        computer_strategy_always_betray,
        computer_strategy_always_cooperate,
        computer_strategy_tit_for_tat,
        computer_strategy_C,
        computer_strategy_D,
        computer_stratergy_Xb,
        computer_stratergy_Xc
    ]
    print("Choose computer strategy:")
    for i, strategy in enumerate(strategies):
        print(f"{i + 1}. {strategy.__name__}")
        
    computer_strategy_choice1 = int(input("Enter the number for computer strategy 1: ")) - 1
    computer_strategy1 = strategies[computer_strategy_choice1]
    
    computer_strategy_choice2 = int(input("Enter the number for computer strategy 2: ")) - 1
    computer_strategy2 = strategies[computer_strategy_choice2]
    player1_score = 0
    player2_score = 0
    computer_choice1 = "cooperate"
    computer_choice2 = "cooperate"
    for round_num in range(1, rounds + 1):
        #print(f"\nRound {round_num}:")
        computer_choice1 = computer_strategy1(computer_choice2)
        computer_choice2 = computer_strategy2(computer_choice1)


        reward_player1, reward_player2 = prisoner_dilemma(computer_choice2, computer_choice1)

        player1_score = reward_player1 + player1_score
        player2_score = reward_player2 + player2_score

        #print(f"Your Score: {player1_score}\tComputer's Score: {player2_score}")
        add_data(data_list, round_num, player1_score, player2_score)
        
    print("\nGame Over!")
    print(f"Computer 1 Score: {player1_score}\tComputer 2 Score: {player2_score}")
    #display_data(data_list)
    excel(data_list)
    
if __name__ == "__main__":
    main()
