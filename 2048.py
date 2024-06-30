import random

Moves = set(['A', 'a', 'W', 'w', 'S', 's', 'D', 'd'])

def initBoard():
    board = [[0,0,0,0] for _ in range(4)]
    i = random.randrange(0,3)
    j = random.randrange(0,3)
    k = random.randrange(0,3)
    l = random.randrange(0,3)
    while i == k and j == l:
        k = random.randrange(0,3)
        l = random.randrange(0,3)
    board[i][j]  = 2
    board[k][l]  = 2
    return board

def printBoard(board):
    for row in board:
        for number in row:
            s = "{:>4}".format(number)
            print(s, end=',')
        print()

def explainGame():
    print("welcome to 2048")
    print("The commands are as follows:")
    print("'W' is to move Up")
    print("'S' is to move Down")
    print("'A' is to move Left")
    print("'D' is to move Right")
    print('Good Luck!')

def getCommand():
    move = input("Enter your Command: ")
    while move not in Moves:
        move = input("Enter only A, W, S, D: ")
    return move.lower()


def moveRight(board):
    moved = False
    for row in board:
            updates = {}
            # print(row)
            for i in range(2, -1, -1):
                if row[i] == 0:
                    continue
                # print(f'i: {i}')
                moveright = -1
                for j in range(i+1, 4):
                    # print(f'j: {j}')
                    if row[i] == row[j]:
                        # print(f'gound same, i,j: {i},{j}')
                        updates[j] = 2 * row[j]
                        row[j] = -1
                        row[i] = 0
                        moved = True
                        break
                    if row[j] == 0:
                        # print(f'Move right: {moveright}')
                        moveright = j
                    else:
                        break
                if moveright != -1:
                    moved = True
                    row[moveright] = row[i]
                    row[i] = 0
            for index, val in updates.items():
                row[index] = val
    return board, moved

def moveDown(board):
    #transpose board
    board = [[row[i] for row in board] for i in range(len(board[0]))]
    #move right
    board, moved = moveRight(board)
    #transpose again
    board = [[row[i] for row in board] for i in range(len(board[0]))]
    return board, moved

def moveLeft(board):
    #reverse each row
    board = [row[::-1] for row in board]
    #move right
    board, moved = moveRight(board)
    #reverse result
    board = [row[::-1] for row in board]
    return board, moved

def moveUp(board):
    #transpose board
    board = [[row[i] for row in board] for i in range(len(board[0]))]
    #move right
    board, moved = moveLeft(board)
    #transpose again
    board = [[row[i] for row in board] for i in range(len(board[0]))]
    return board, moved

def performMove(board, move):
    if move == 'd':
        return moveRight(board)
    if move == 's':
        return moveDown(board)
    if move == 'a':
        return moveLeft(board)
    if move == 'w':
        return moveUp(board)

    
def updateBoard(board, move):
    board, moved = performMove(board, move)
    if not moved:
        print("you didnt do anything")
        return board
    won = False
    lost = True
    emptyslots = []
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for i in range(4):
        if won:
            break
        for j in range(4):
            if board[i][j] == 0:
                lost = False
                emptyslots.append((i,j))
            elif board[i][j] == 2048:
                won = True
                break
            elif lost:
                for dx, dy in directions:
                    newrow, newcol = i + dx, j + dy
                    if 0 <= newrow < 4 and 0 <= newcol < 4:
                        if board[i][j] == board[newrow][newcol]:
                            lost = False
                            break
    if won:
        print('you Won!!')
        printBoard(board)
        quit()
    if lost:
        print('sorry, you cant make any more moves, you lost')
        quit()
    if emptyslots:
        x,y = random.choice(emptyslots)
        board[x][y] = 2
    return board
    


if __name__ =="__main__":
    board = initBoard()
    explainGame()
    while True:
        printBoard(board)
        move = getCommand()
        board = updateBoard(board, move)
