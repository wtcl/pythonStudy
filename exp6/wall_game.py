import random


# 打印棋盘
def drawboard(board):
    print("   |   |   ")
    print(" " + board[1] + ' | ' + board[2] + ' | ' + board[3] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + ' | ' + board[8] + ' | ' + board[9] + " ")
    print("   |   |   ")


# 让玩家来选择X或者是O
def xoro():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('你要选X还是O?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


# 决定谁先走从，此处随机选择
def gofist():
    if random.randint(0, 2) == 0:
        return '电脑'
    else:
        return '玩家'


# 更新位置列表
def refreshsite(board, letter, move):
    board[move] = letter


# 判断玩家是否获胜
def iswin(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


# 判断游戏板上的格子是否为空
def isfree(board, move):
    return board[move] == ' '


# 让玩家输入落子的格子的编号
def playermove(board):
    move = ' '
    # 如果输入错误，或者输入的位置已经有棋子，会要求重新输入
    while move not in list('123456789') or not isfree(board, int(move)):
        print('你要落子的位置是？(1-9)')
        move = input()
    return int(move)


# 从落子列表选择一个落子
def randchoose(board, movelist):
    possiblemoves = []
    for i in movelist:
        if isfree(board, i):
            possiblemoves.append(i)

    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None


# 计算机移动
def cmove(board, computerletter):
    if computerletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

    for i in range(0, 10):
        boardc = board[::]
        if isfree(boardc, i):
            refreshsite(boardc, computerletter, i)
            if iswin(boardc, computerletter):
                return i

    for i in range(0, 10):
        boardc = board[::]
        if isfree(boardc, i):
            refreshsite(boardc, playerletter, i)
            if iswin(boardc, playerletter):
                return i

    move = randchoose(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if isfree(board, 5):
        return 5

    return randchoose(board, [2, 4, 6, 8])


def isboardfull(board):
    for i in range(1, 10):
        if isfree(board, i):
            return False
    return True


if __name__ == "__main__":
    print('欢迎来到井字棋游戏!')
    while True:
        theBoard = [' '] * 10
        playerletter, computerletter = xoro()
        turn = gofist()
        print(turn + '先走。')
        gameIsplaying = True

        while gameIsplaying:
            if turn == '玩家':
                drawboard(theBoard)
                move = playermove(theBoard)
                refreshsite(theBoard, playerletter, move)

                if iswin(theBoard, playerletter):
                    drawboard(theBoard)
                    print('恭喜，你赢了！')
                    gameIsplaying = False
                else:
                    if isboardfull(theBoard):
                        drawboard(theBoard)
                        print('平局！')
                        break
                    else:
                        turn = '电脑'
            else:
                # 电脑下
                move = cmove(theBoard, computerletter)
                refreshsite(theBoard, computerletter, move)
                if iswin(theBoard, computerletter):
                    drawboard(theBoard)
                    print('电脑赢了，你输了！')
                    gameIsplaying = False
                else:
                    if isboardfull(theBoard):
                        drawboard(theBoard)
                        print('平局！')
                        break
                    else:
                        turn = '玩家'

        print('你还想要再玩一次吗？(yes or no)')
        decide = input()
        if decide not in ["yes", "Yes", "YES", "y", "yes"]:
            break
