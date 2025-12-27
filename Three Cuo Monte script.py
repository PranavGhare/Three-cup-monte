from random import shuffle

#Game List
mylist = [' ', ' ', 'O']

# Function to shuffle the list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Function to get the player's guess
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)

# Function to check if the player's guess is correct
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct! You found the O!")
    else:
        print("Wrong guess. Try again!")
    print(f"The list was: {mylist}")    

# Main game logic
shuffled_list = shuffle_list(mylist)    
guess = player_guess()
check_guess(shuffled_list, guess)
