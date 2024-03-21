import random

def play_game(player_choice):
    """
    Play a round of rock-paper-scissors game against the computer.
    
    Args:
        player_choice (str): The player's choice ('rock', 'paper', or 'scissors').
        
    Returns:
        str: The result of the game ('win', 'lose', or 'draw').
    """
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice 
