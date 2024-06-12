import os
import random

def clear_screen()->None:
    os.system('clear')   #For screen clearing the entered number 

def move_from_player(player_name:str,choices:list)->str:
    while True:
        move = input(f"Player {player_name}, enter a(rock,paper or scissor): ")
        if move in choices:
            return move
        print("Invalid input")

def move_from_comp(moves:list)->str:
    move=random.choice(moves)
    return move

def win(move_p:str, move_comp:str)->str:
    if move_comp==move_p:
        result="Tie" 
    elif move_comp=="rock":
            if(move_p=="paper"):
                result="Win"
            else:
                 result="Lose"
    elif move_comp=="paper":
            if(move_p=="scissor"):
                result="Win"
            else:
                 result="Lose"
    else:
            if(move_p=="rock"):
                result="Win"
            else:
                 result="Lose"
    return result


def play_game(player:str,round:int)->None:
    score_c=0
    score_p=0
    while round:
        choices=["rock","paper","scissor"]
        move_p = move_from_player(player,choices)
        move_c =move_from_comp(choices)
        result=win(move_p,move_c)
        print(f"Player move: {move_p}")
        print(f"Computer move: {move_c}")
        print(f"Result: {result}")
        if(result=="Win"):
             score_p+=1
        elif(result=="Lose"):
             score_c+=1
        round-=1
    print(f"Player {player} score :{score_p}")
    print(f"Computer score :{score_c}")


input("Press Enter to start the Game")
while True:
    print("-----------------------------------------------")
    print("    Welcome to Rock,Paper and Scissor Game     ")
    print("-----------------------------------------------")
    print("                   RULES                       ")
    print("-----------------------------------------------")
    print("*Win the more round than Computer              ")
    print("*Enter the Input in lowercase                  ")
    print("*Select the number of round as per need        ")
    print("-----------------------------------------------")
    print("\n")
    player_name = input("Enter Player name: ")
    rounds = int(input("Enter the number of rounds(3,5,7): "))
    play_game(player_name,rounds)
    play_again = input("Do you want to play again? (no to discontinue):").lower()
    if play_again=='no':
        break
    clear_screen()