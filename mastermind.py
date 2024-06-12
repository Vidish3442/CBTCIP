import os

def clear_screen() -> None:
    os.system('clear')   #For screen clearing the entered number 

def number_from_player(player_name:str)->str:
    while True:
        num = input(f"Player {player_name}, enter a multi-digit number to be guessed: ")
        if num.isdigit() and len(num) > 1:
            return num 
        print("Invalid input. Please enter a multi-digit number.")

def guess_from_player(player_name:str, l:int)->str:
    while True:
        num = input(f"Player {player_name}, enter a guess of {l} numbers: ")
        if num.isdigit() and len(num) == l:
            return num
        print("Invalid input. Please enter a number with the same number of digits as the original number.")

def give_hint(number_to_guess:str, guess:str)->str:
    hint = ""
    for i in range(len(number_to_guess)):
        if number_to_guess[i] == guess[i]:
            hint += "O"  # correct digit in correct position
        elif guess[i] in number_to_guess:
            hint += "X"  # correct digit in incorrect position
        else:
            hint += "!"  # incorrect digit
    return hint


def play_game(player1_name:str, player2_name:str)->None:
    number_to_guess = number_from_player(player1_name)       # Player 1 sets the number
    clear_screen()
    print(f"Player {player1_name} has set the number. Good luck, Player {player2_name}!")

    # Player 2 tries to guess the number
    num_guesses_p2 = 0
    while True:
        guess = guess_from_player(player2_name, len(number_to_guess))
        num_guesses_p2 += 1
        if guess == number_to_guess:
            if(num_guesses_p2==1):
                print(f"Congratulations, Player {player2_name}! You guessed the number in {num_guesses_p2} tries.You are a Mastermind")
                break
            else:
                print(f"Congratulations, Player {player2_name}! You guessed the number in {num_guesses_p2} tries.")
                break
        else:
            print(f"Hint: {give_hint(number_to_guess, guess)}")

    if(num_guesses_p2==1):
        return     # As guess cannot be less than 1
    
    # Player 2 sets the number
    number_to_guess = number_from_player(player2_name)
    clear_screen()
    print(f"Player {player2_name} has set the number. Good luck, Player {player1_name}!")

    # Player 1 tries to guess the number
    num_guesses_p1 = 0
    while True:
        guess = guess_from_player(player1_name, len(number_to_guess))
        num_guesses_p1 += 1
        if guess == number_to_guess:
            if num_guesses_p1 < num_guesses_p2:
                print(f"Congratulations, Player {player1_name}! You guessed the number in {num_guesses_p1} tries, which is less than Player {player2_name}'s {num_guesses_p2} tries. You are the Mastermind!")
            else:
                print(f"Congratulations, Player {player1_name}! You guessed the number in {num_guesses_p1} tries, but it's not enough to beat Player {player2_name}'s {num_guesses_p2} tries. Player {player2_name} is the Mastermind!")
            break
        else:
            print(f"Hint: {give_hint(number_to_guess, guess)}")


input("Press Enter to start the Game")
while True:
    print("-----------------------------------------------")
    print('          Welcome to Mastermind Game           ')
    print("-----------------------------------------------")
    print("                   RULES                       ")
    print("-----------------------------------------------")
    print("*Win the Game before the other Player          ")
    print("*Guess the number in the least number of tries ")
    print("*The number can be repeative so Careful        ")
    print("-----------------------------------------------")
    print("                 For Hints                     ")
    print("0 means correct digit in correct position      ")
    print("X means correct digit in incorrect position    ")
    print("! means incorrect digit                        ")
    print("-----------------------------------------------")
    print("\n")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    play_game(player1_name, player2_name)
    play_again = input("Do you want to play again? (no to discontinue):").lower()
    if play_again=='no':
        break
    clear_screen()