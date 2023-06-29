import sys
import random
import numpy as np



def gameMode():
    while True :
        mode=int(input('Welcome to N-puzzle game. Enter 3 for 3*3 mode. Enter 4 for 4*4 mode .……. Enter 10 for 10*10 mode.'))
        if mode == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            return mode


def board(mode):
    BoardList=[]
    OriginList=[]
    if mode == 3:
        for i in range(9):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 4:
        for i in range(16):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 5:
        for i in range(25):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 6:
        for i in range(36):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 7:
        for i in range(49):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 8:
        for i in range(64):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 9:
        for i in range(81):
            BoardList.append(i)
            OriginList.append(i)
    elif mode == 10:
        for i in range(100):
            BoardList.append(i)
            OriginList.append(i)
    else:
        return False

    rowNumber=mode
    boardMatrix = []
    originMatrix=[]

    while BoardList !=[]:
        boardMatrix.append(BoardList[:rowNumber])
        BoardList = BoardList[rowNumber:]
    boardMatrix=np.array(boardMatrix)


    while OriginList !=[]:
        originMatrix.append(OriginList[:rowNumber])
        OriginList = OriginList[rowNumber:]
    originMatrix=np.array(originMatrix)
    a=random.randint(0,mode-1)
    b=random.randint(0,mode-1)
    directionList=['l','r','u','d']
    for i in range(10000):
        position=random.choice(directionList)
        if position=='u':
            if a!=mode-1:
                boardMatrix[a][b],boardMatrix[a+1][b]=boardMatrix[a+1][b],boardMatrix[a][b]
            else:
                continue
        if position=='d':
            if a!=0:
                boardMatrix[a][b],boardMatrix[a-1][b]=boardMatrix[a-1][b],boardMatrix[a][b]
            else:
                continue
        if position=='l':
            if b!=mode-1:
                boardMatrix[a][b],boardMatrix[a][b+1]=boardMatrix[a][b+1],boardMatrix[a][b]
            else:
                continue
        if position=='r':
            if b!=0:
                boardMatrix[a][b],boardMatrix[a][b-1]=boardMatrix[a][b-1],boardMatrix[a][b]
            else:
                continue
    return boardMatrix,originMatrix




def findZero(boardMatrix): 
    x= None
    y= None
    list1=np.argwhere(boardMatrix==0)
    x=list1[0][0]
    y=list1[0][1]
    return x,y

def draw_board(mode,boardMatrix):
    newBoard=boardMatrix.tolist()
    for a, element in enumerate(newBoard):
        for b, element in enumerate(newBoard):
            if newBoard[a][b] == 0:                                              
                print('  ' , end=' ')
            else:
                 print( '{:02d}' .format(newBoard[a][b]), end=' ')
        print()

def direction(x,y,mode):
    if 0<x<mode-1 and 0<y<mode-1:
        direction = input("Enter move (l-left,r-right,u-up,d-down)>")

    elif 0<x<mode-1 and y==0:
        direction = input("Enter move (l-left,u-up,d-down)>")

    elif 0<x<mode-1 and y==mode-1:
        direction = input("Enter move (r-right,u-up,d-down)>")

    elif x==0 and 0<y<mode-1:
        direction = input("Enter move (r-right,u-up,l-left)>")

    elif x==mode-1 and 0<y<mode-1:
        direction = input("Enter move (r-right,d-down,l-left)>")

    elif x==0 and y==0:
        direction = input("Enter move (u-up,l-left)>")

    elif x==0 and y==mode-1:
        direction = input("Enter move (r-right,u-up)>")

    elif x==mode-1 and y==0:
        direction = input("Enter move (d-down,l-left)>")

    elif x==mode-1 and y==mode-1:
        direction = input("Enter move (d-down,r-right)>")

    return direction



def judge(boardMatrix,originMatrix):
    list1=boardMatrix.tolist()
    list2=originMatrix.tolist()
    if list1==list2:
        return True
    else:
        return False



def main():
    mode=gameMode()
    a=board(mode)
    boardMatrix=a[0]
    originMatrix=a[1]
    b=findZero(boardMatrix)
    x=b[0]        
    y=b[1]
    move=0
    draw_board(mode,boardMatrix)
    while True:
        direct=direction(x,y,mode)
        if direct=='u':
            if x!=mode-1:
                boardMatrix[x][y]=boardMatrix[x+1][y]
                boardMatrix[x+1][y]=0
                x+=1
        if direct=='d':
            if x!=0:
                boardMatrix[x][y]=boardMatrix[x-1][y]
                boardMatrix[x-1][y]=0
                x-=1
        if direct=='l':
            if y!=mode-1:
                boardMatrix[x][y]=boardMatrix[x][y+1]
                boardMatrix[x][y+1]=0
                y+=1
        if direct=='r':
            if y!=0:
                boardMatrix[x][y]=boardMatrix[x][y-1]
                boardMatrix[x][y-1]=0
                y-=1
        draw_board(mode,boardMatrix)
        move+=1
        print('you take',move,'times')
        if judge(boardMatrix,originMatrix) is True:
            print('Congratulations,you finish it through',move,'times')
            again=input('Enter ‘n’ to start a new game or enter ‘q’ to end the game >')
            if again=='n':
                gameMode()
            if again=='q':
                sys.exit()




if __name__ == '__main__':
    main()

    









