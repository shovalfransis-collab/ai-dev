

# print ([name [0] for name in ['hi' , 'bye', 'lol']])



# def introduce(firstname: str, lastname: str) -> None:
#     """
#     Prints an introduction using the provided first and last name.

#     Args:
#         firstname (str): The first name to introduce.
#         lastname (str): The last name to introduce.
#     """
#     print(f'my first name is {firstname} and my last name is {lastname}')
    
# introduce(firstname='shoval', lastname='fransis')


from random import shuffle

# This function shuffles a list and returns a new one.
def new_shuffle(lst):
    # To avoid shuffling the original list passed by caller,
    # make a new list copy, shuffle it, and return the shuffled one.
    lst_copy = lst[:]
    shuffle(lst_copy)
    return lst_copy

# Get the player's guess: make sure they pick 1, 2, or 3 (as position indices)
def guess():
    player_guess = input('Pick a position: 1, 2, or 3: ')
    while player_guess not in ['1', '2', '3']:
        player_guess = input('Invalid pick. Pick a position: 1, 2, or 3: ')
    return int(player_guess) - 1  # change to 0-based index

# Check if the guess is correct
def check(shuffled_list, player_guess):
    # We look at the spot the player picked in the list.
    # If there is a '0' in that spot, the player wins!
    if shuffled_list[player_guess] == '0':
        print('Good! You found the 0!')
    else:
        print('Try again. The shuffled list was:', shuffled_list)

# Game flow:
base_list = [" ", "0", " "]
shuffled_list = new_shuffle(base_list)
print("Shuffled list:", shuffled_list)  # For debugging, or remove in real game

player_guess = guess()
check(shuffled_list, player_guess)