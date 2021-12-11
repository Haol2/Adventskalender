import time


def printBoard(board):
    for line in board:
        print(line)

def printBoards(boards):
    i = 1
    for board in boards:
        print(str(i) + ": ")
        printBoard(board)
        print("")
        i += 1

def markNumber(boards, drawn):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                number = boards[i][j][k]
                if not checkMarked(number):
                    if int(number) == drawn:
                        boards[i][j][k] = "|" + number + "|"

def checkMarked(number):
    if number.startswith("|"):
        return True

def checkIfWon(boards):
    #check lines
    for b in range(len(boards)):
        board = boards[b]
        for line in board:
            i = 0
            for number in line:
                if checkMarked(number):
                    i += 1
            if i == 5:
                print("board number " + str(b+1) + " has won!!!")
                printBoard(board)
                return board

    #check cols
    for b in range(len(boards)):
        board = boards[b]
        for index in range(5):
            i = 0
            for line in board:
                if checkMarked(line[index]):
                    i += 1
            if i == 5:
                print("board number " + str(b+1) + " has won!!!")
                printBoard(board)
                return board

def calculateResult(board, draw):
    result = 0
    for line in board:
        for number in line:
            if not checkMarked(number):
                result += int(number)

    return result*int(draw)

f = open("input4.txt", "r")

list = f.read().split("\n\n")
draws = list[0].split(",")
boards = list[1:]
for i in range(len(boards)):
    boards[i] = boards[i].split("\n")
    for j in range(len(boards[i])):
        boards[i][j] = boards[i][j].split()

'''-------------------------------------------------------------------'''

print("draws: " + str(draws))
print("boards: ")
printBoards(boards)

#---marking the drawn numbers



for draw in draws:
    markNumber(boards, int(draw))
    board = checkIfWon(boards)
    if board:
        print("last drawn: " + str(draw))
        print("score result = " + str(calculateResult(board, draw)))
        break