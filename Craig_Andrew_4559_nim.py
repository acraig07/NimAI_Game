# nim.py
# game of Nim, CSE 5120, Fall 2021
# programmer: Andrew Craig

import random
random.seed()

# create a game of nim with 3 piles of k stones
def nim_setup(k):
    mynim = [k,k,k]
    return mynim

# display the state of the game of nim
def show_nim(nim):
    for i in range(3):
        print "pile %d: " % (i+1),
        for i in range(nim[i]):
            print "@ ",
        print ""
    print "\n"

# play function
# determines who turn it is and the winner
def play_nim(k):
    print "Three piles of %d stones ... Start the Game!" % k,
    print "\n\n"
    game = nim_setup(k)
    show_nim(game)
    
    player_turn = None
    player_trun = True # used to track whose turn it is for winner determination 

    while game != [0,0,0]:
        player_moves(game)
        player_turn = False
        if (game != [0,0,0]):
            computer_moves(game)
            player_turn = True
        else:
            break
            
    if (player_turn == True):
        print "Computer took the last stone --- Player Wins!!!"

    else:
        print "Player took the last stone --- Computer Wins!!!"
        

# function that conrtols the human players moves
def player_moves(nim):
    player_pile = input("Choose pile [1-3]: ")
    while (player_pile <= 0 or player_pile >= 4 or nim[player_pile - 1] == 0):
        player_pile = input("Pile is empty/invalid choose another pile: ")
    player_stones = input("You take how many stones from pile %s? " %player_pile)
    while (player_stones > nim[player_pile -1] or player_stones <= 0):
        player_stones = input("Amount of stones chosen exceeds amount in pile, choose another value: ")
    print "You took %s stone(s) from pile %s" %(player_stones, player_pile)
    print "\n"
    print "These piles of stone remain --- Continue to play!!!\n"
    
    if (player_pile == 1):
        temp = nim[0]
        nim[0] = nim[0] - player_stones
        show_nim(nim)
    elif (player_pile == 2):
        temp = nim[1]
        nim[1] = nim[1] - player_stones
        show_nim(nim)
    elif (player_pile == 3):
        temp = nim[2]
        nim[2] = nim[2] - player_stones
        show_nim(nim)
    return

# function that controls the computers moves
def computer_moves(nim):
    if (nim[0] and nim[1] and nim[2] != 0):
        computer_pile = random.randint(1,3)
        temp = nim[computer_pile - 1]
        computer_stones = random.randint(1,temp)
        nim[computer_pile - 1] = temp - computer_stones
    else:
        computer_pile = random.randint(1,3)
        temp1 = nim[computer_pile - 1]
        while temp1 == 0:
            computer_pile = random.randint(1,3)
            temp1 = nim[computer_pile - 1]
        temp = nim[computer_pile - 1]
        if (temp == 1):
            computer_stones = 1
        else:
            computer_stones = random.randint(1,temp)
        nim[computer_pile - 1] = temp - computer_stones

    print "Computer took %s stone(s) from pile %s\n\n" %(computer_stones, computer_pile)
    print "These piles of stone remain --- Continue to play!!!\n"
    show_nim(nim)
    
    return
