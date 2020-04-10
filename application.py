import random

# Keep track of which player is going
turn = 1

# Positions starting at 0
player1_pos = 0
player2_pos = 0

# Sums required to be rolled when position = index
board1 = [6, 5, 4, 7, 10, 8, 9, 4, 3, 12]
board2 = [10, 4, 8, 9, 5, 6, 4, 7, 2, 11]

# Random roll of each die
class Roll:
  def __init__(self):
    self.die1 = random.randint(1, 6)
    self.die2 = random.randint(1, 6)

# Returns 2 dice and their sum in a dictionary
def roll_dice():
    newRoll = Roll()
    roll = {'roll1': newRoll.die1, 'roll2': newRoll.die2, 'sum': newRoll.die1 + newRoll.die2}
    return roll

# Player 1 move forward 1
def player1_addpos():
    global player1_pos
    player1_pos = player1_pos + 1
    if player1_pos == 10:
        print("Player 1 won!")
        reset()

# Player 2 move forward 1
def player2_addpos():
    global player2_pos
    player2_pos = player2_pos + 1
    if player2_pos == 10:
        print("Player 2 won!")
        reset()

# Get position of player 1
def player1_getpos():
    return player1_pos

# Get position of player 2
def player2_getpos():
    return player2_pos

# Reset player positions
def reset():
    global player1_pos
    global player2_pos
    global turn
    player1_pos = 0
    player2_pos = 0
    turn = 1

# Rolls dice for player 1 and decides if a move can be made
def player1_move():
    newRoll = roll_dice()
    d1 = newRoll['roll1']
    d2 = newRoll['roll2']
    sum = newRoll['sum']
    print("Die 1: " + str(d1))
    print("Die 2: " + str(d2))
    print("Sum: " + str(sum))

    if sum == board1[player1_pos]:
        player1_addpos()
        print("You collected the token and you're moving on!")
    else:
        print("You did not collect the token.")

# Rolls dice for player 2 and decides if a move can be made
def player2_move():
    newRoll = roll_dice()
    d1 = newRoll['roll1']
    d2 = newRoll['roll2']
    sum = newRoll['sum']
    print("Die 1: " + str(d1))
    print("Die 2: " + str(d2))
    print("Sum: " + str(sum))

    if sum == board2[player2_pos]:
        player2_addpos()
        print("You collected the token and you're moving on!")
    else:
        print("You did not collect the token.")

# General display to begin player 1's turn
def display1():
    print("*****Player 1's Turn*****")
    print("Player 1 position: " + str(player1_pos))
    print("Player 2 position: " + str(player2_pos))
    print("You must roll a " + str(board1[player1_pos]))

# General display to begin player 1's turn
def display2():
    print("*****Player 2's Turn*****")
    print("Player 2 position: " + str(player2_pos))
    print("Player 1 position: " + str(player1_pos))
    print("You must roll a " + str(board2[player2_pos]))
            

# main
while 1:
    if turn == 1:
        display1()
        cmd = input("Type r to roll, q to quit, or 0 to reset: ")
        if cmd == "r":
            player1_move()
        elif cmd == "q": 
            break
        elif cmd == "0":
            reset()
        else: 
            cmd = input("Type r to roll, q to quit, or 0 to reset: ")
        turn = 2
    elif turn == 2:
        display2()
        cmd = input("Type r to roll, q to quit, or 0 to reset: ")
        if cmd == "r":
            player2_move()
        elif cmd == "q": 
            break
        elif cmd == "0":
            reset()
        else: 
            cmd = input("Type r to roll, q to quit, or 0 to reset: ")
        turn = 1
    else:
        break

  
