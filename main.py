import sys
import math


# Автогенерированный код ниже направлен на то, чтобы помочь вам разобрать
# стандартный ввод в соответствии с постановкой задачи.

# w: ширина здания.
# h: высота здания.
minX = 0
minY = 0
maxX, maxY = [int(i) for i in input().split()]
_ = input()
x, y = [int(i) for i in input().split()]
while True:
    bomb_dir = input()
    if bomb_dir == 'U':
        minX = x
        maxX = x
        maxY = y
    elif bomb_dir == 'UR':
        minX = x
        maxY = y
    elif bomb_dir == 'R':
        minY = y
        maxY = y
        minX = x
    elif bomb_dir == 'DR':
        minY = y
        minX = x
    elif bomb_dir == 'D':
        minX = x
        maxX = x
        minY = y
    elif bomb_dir == 'DL':
        minY = y
        maxX = x
    elif bomb_dir == 'L':
        minY = y
        maxY = y
        maxX = x
    elif bomb_dir == 'UL':
        maxX = x
        maxY = y
    x = (minX + maxX)//2;
    y = (minY + maxY)//2;
    print(x,y)