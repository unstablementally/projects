import os
import time

def clear_screen():
    # Check the operating system and use the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def check_winner(screen_choice):
    # Define winning combinations
    winning_combinations = [
        (0, 1, 2),  # Horizontal top row
        (3, 4, 5),  # Horizontal middle row
        (6, 7, 8),  # Horizontal bottom row
        (0, 3, 6),  # Vertical left column
        (1, 4, 7),  # Vertical middle column
        (2, 5, 8),  # Vertical right column
        (0, 4, 8),  # Diagonal from top-left to bottom-right
        (2, 4, 6)   # Diagonal from top-right to bottom-left
    ]
    
    # Check each winning combination
    for combo in winning_combinations:
        if screen_choice[combo[0]] == screen_choice[combo[1]] == screen_choice[combo[2]] and screen_choice[combo[0]] not in "abcdefghi":
            return screen_choice[combo[0]]  # Return the winner ("X" or "O")
    return None  # No winner

# Initialize the game board with letters for reference
screen_choice = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
screen = f"""|{screen_choice[0]}|{screen_choice[1]}|{screen_choice[2]}|
|{screen_choice[3]}|{screen_choice[4]}|{screen_choice[5]}|
|{screen_choice[6]}|{screen_choice[7]}|{screen_choice[8]}|"""
print(screen)

player_1 = "O"
player_2 = "X"
game_end = False

while not game_end:
    # Player 1's turn
    player_1_answer = False
    while not player_1_answer:
        player_1_input = input("Pick a letter for where you want to put O: ")
        if player_1_input != "O" and player_1_input != "X":
            if player_1_input in screen_choice:
                p1_index = screen_choice.index(player_1_input)
                screen_choice[p1_index] = "O"
                player_1_answer = True
            else:
                print("Incorrect input.")
        else:
            print("You cannot use an already used spot.")
        # Update the screen after the move
    screen = f"""|{screen_choice[0]}|{screen_choice[1]}|{screen_choice[2]}|
|{screen_choice[3]}|{screen_choice[4]}|{screen_choice[5]}|
|{screen_choice[6]}|{screen_choice[7]}|{screen_choice[8]}|"""
    clear_screen()
    print(screen)
    
    # Check for a winner after Player 1's move
    winner = check_winner(screen_choice)
    if winner:
        print(f"The winner is {winner}!")
        game_end = True
        break

    # Player 2's turn
    player_2_answer = False
    while not player_2_answer:
        player_2_input = input("Pick a letter for where you want to put X: ")
        if player_2_input != "O" and player_2_input != "X": 
            if player_2_input in screen_choice:
                p1_index = screen_choice.index(player_2_input)
                screen_choice[p1_index] = "X"
                player_2_answer = True
            else:
                print("Incorrect input.")
        else:
            print("You cannot use an already used spot.")
        # Update the screen after the move
    screen = f"""|{screen_choice[0]}|{screen_choice[1]}|{screen_choice[2]}|
|{screen_choice[3]}|{screen_choice[4]}|{screen_choice[5]}|
|{screen_choice[6]}|{screen_choice[7]}|{screen_choice[8]}|"""
    clear_screen()
    print(screen)
    
    # Check for a winner after Player 2's move
    winner = check_winner(screen_choice)
    if winner:
        print(f"The winner is {winner}!")
        game_end = True
