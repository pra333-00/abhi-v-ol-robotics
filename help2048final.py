# Steps and SEQUENCE of functions so that we do not go wrong again
# 1. Set up the board, using a list of lists. Create a temporary board.
# 2. Create functions that will merge left, right, up, and down. Will create functions to reverse and transpose the list of lists to do this
# 3. Set up the start of the game, creating an empty gameboard filled with two random values.
# 4. Set up the rounds of the game, where the user will have the option to megre in any one of the four directions, and after they move then new board will display
# 5. Set up adding a new value each time.
# 6. Set up functions testing if the user has won or lost.

import random
import copy

board = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]]
# Creating the board size variable
boardSize = 4

# This functon will print out the current bard in the way we want
def display():
    # Finding out the larggest value
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    # Setting the spaxces according to width of maximum value
    width = len(str(largest))
    
    for row in board:
        current_Row = "|"
        for element in row:
            # If the element is 0, prinyt a space
            if element == 0:
                current_Row += " "*width + "|"
            # If not, we should print the value
            else:
                current_Row += (" "*(width - len(str(element)))) + str(element) + "|"

        # Print the generated row
        print(current_Row)
    print()

display()


# This function merges one row left
def mergeOneRowLeft(row):
    # Move everything as far left as possible
    
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0 ,-1):
            #Test if there is any empty space, move if yes
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
        
    # Merge everything to the left
    for i in range(boardSize - 1):
        #Testing if current value is idential to the one next to it
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
            
    # Move everything to the left again
    for i in range(boardSize - 1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    
    return row

# This function merges the whole board to the left  
def mergeLeft(currentBoard):
    # Merge every row in the board left
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowLeft(currentBoard[i])
    
    return currentBoard

# This function reverses the order of one row
def reverse(row):
    new = []
    # Add all elemtns of the same rowto a new list in reverse order
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new

# This function merges the whole board right
def mergeRight(currentBoard):
    # Looking at every row in board
    for i in range(boardSize):
        #Reverses the row, merges to the left, then reverses back
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowLeft(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

# This function transposes the whole board
def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

def mergeUp(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = mergeLeft(currentBoard)
    currentBoard = transpose(currentBoard)
    
    return currentBoard

def mergeDown(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = mergeRight(currentBoard)
    currentBoard = transpose(currentBoard)
    
    return currentBoard

# Creating and adding values IMP: as per rules of 2048 we know 4 has
# 12.5% chance of appearing so we incorporate that
def pickNewValue():
    if random.randint(1,8) == 1:
        return 4
    else:
        return 2

# Here we constantly check to add new values    
def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)
    
    while board[rowNum][colNum] != 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)
    
    board[rowNum][colNum] = pickNewValue()
    
    
def won():
    for row in board:
        if 2048 in row:
            return True
        return False

# Method of explanation to audience -
# Imagine I have one square karate board and two identical copies of it
# Before I can use the karate board for training,
# I want to see if it breakes properly
# So i take karate board copy 2 and keep it beside me
# and then i proceed to test breaking copy 1 from all 4 sides
# I then compare if copy 1 broke or is still just like copy 2 from both sides
# If all 4 times it does not break 
def lost():
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)
    
    tempboard1 = mergeDown(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = mergeUp(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempboard1 = mergeLeft(tempBoard1)
            if tempboard1 == tempBoard2:
                tempBoard1 = mergeRight(tempboard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False


# Initiating the actual game

board = []

for i in range(boardSize):
    row=[]
    for j in range(boardSize):
        row.append(0)
    board.append(row)
    
numStart = 2
while numStart > 0:
    rowNum = random.randint(0,boardSize - 1)
    colNum = random.randint(0, boardSize - 1)
    
    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numStart -= 1
        
print("Start Game, use WASD commands to move")

display()

gameOver = False

while not gameOver:
    move= input("Enter W or A or S or D: ")
    
    validInput = True
    
    tempBoard = copy.deepcopy(board)
    
    if move == 'W':
        board = mergeUp(board)
    elif move == 'A':
        board = mergeLeft(board)
    elif move == 'S':
        board = mergeDown(board)
    elif move == 'D':
        board = mergeRight(board)
    else:
        validInput = False
    
    
    
    if not validInput:
        print("Invalid input, try again")
    
    else:
        if board == tempBoard:
            print("Try a different direction")
        else:
            
            if won():
                display()
                print("YOU WIN!")
                gameOver = True
            else: 
                addNewValue()
                display()
                if lost() == True: 
                    print("YOU LOST!")
                    gameOver = True
        
    
