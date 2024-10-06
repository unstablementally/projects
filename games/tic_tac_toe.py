import os
import time

def clear_screen():
    # Check the operating system and use the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# https://docs.python.org/3/library/os.html
screen_choice = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
screen = f"""|{screen_choice[0]}|{screen_choice[1]}|{screen_choice[2]}|
|{screen_choice[3]}|{screen_choice[4]}|{screen_choice[5]}|
|{screen_choice[6]}|{screen_choice[7]}|{screen_choice[8]}|"""
# f-string!!
print(screen)
player_1 = "O"
player_2 = "X"
game_end = False
while not game_end:
    player_1_answer = False
    while not player_1_answer:
        player_1_input = input("Pick a letter for where you want to put O: ")
        if player_1_input in screen_choice:
            p1_index = screen_choice.index(player_1_input)
            screen_choice[p1_index] = "O"
            player_1_answer = True
        else:
            print("Incorrect input.")
        
        # Update the screen after the move
        screen = f"""|{screen_choice[0]}|{screen_choice[1]}|{screen_choice[2]}|
|{screen_choice[3]}|{screen_choice[4]}|{screen_choice[5]}|
|{screen_choice[6]}|{screen_choice[7]}|{screen_choice[8]}|"""
        clear_screen()
        print(screen)
        player_2_answer = False
    while not player_2_answer:
        player_2_input = input("Pick a letter for where you want to put X: ")
        if player_2_input in screen_choice:
            p1_index = screen_choice.index(player_2_input)
            screen_choice[p1_index] = "X"
            player_2_answer = True
        else:
            print("Incorrect input.")
        
        # Update the screen after the move
        screen = f"""|{screen_choice[0]}|{screen_choice[1]}|{screen_choice[2]}|
|{screen_choice[3]}|{screen_choice[4]}|{screen_choice[5]}|
|{screen_choice[6]}|{screen_choice[7]}|{screen_choice[8]}|"""
        clear_screen()
        print(screen)
