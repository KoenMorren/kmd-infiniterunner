import world_generation

boardX = 4
board_render_distance = 5
playerX, playerY = 2, 4
gameBoard = None

def printGameBoard():
    board = [x[:] for x in gameBoard]

    for i, line in enumerate(board):
        if playerY - board_render_distance < i <= playerY:
            if i == playerY:
                line[playerX] = 'X'

            print(' '.join(line))

def handleUserInput(direction):
    global playerX, playerY, gameBoard

    if (direction == 'w'):
        if (playerY >= board_render_distance and gameBoard[playerY - 1][playerX] == 'O'):
            playerY -= 1
        elif (gameBoard[playerY - 1][playerX] == 'O'):
            gameBoard = world_generation.addRow()

    if (direction == 'a'):
        if (playerX != 0 and gameBoard[playerY][playerX - 1] == 'O'):
            playerX -= 1
    
    if (direction == 's'):
        if (playerY != len(gameBoard) - 1 and gameBoard[playerY + 1][playerX] == 'O'):
            playerY += 1

    if (direction == 'd'):
        if (playerX != boardX and gameBoard[playerY][playerX + 1] == 'O'):
            playerX += 1

def main():
    global gameBoard
    gameBoard = world_generation.generate(boardX + 1, board_render_distance)

    while 1 :
        # clear the terminal window
        print(chr(27) + "[2J")

        printGameBoard()

        direction = input('move using wasd: ').lower()

        if (direction in ['w','a','s','d']):
            handleUserInput(direction)

main()