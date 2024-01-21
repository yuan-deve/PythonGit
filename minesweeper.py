import numpy as np
import random
import sys

sys.setrecursionlimit(2000) # set the maximum depth as 2000


class Mines:
    def __init__(self) -> None:
        self.show = ' '
        self.inside = ' '

def check():
    ret = True
    for i in range(10):
        for j in range(10):
            if m[i][j] != 'x':
                if m[i][j].show != ' ' and m[i][j].show != '1' and m[i][j].show != '2' and m[i][j].show != '3' and m[i][j].show != '4' and m[i][j].show != '5' and m[i][j].show != '6' and m[i][j].show != '7' and m[i][j].show != '8':
                    ret = False
                    break
            else:
                if m[i][j].show != '▶':
                    ret = False
                    break
    return ret

        
def display():
    print("\033c")
    print('   \033[32m1 2 3 4 5 6 7 8 9 10\033[0m')
    for i in range(10):
        if i == 9:
            print('\033[32m10\033[0m', end = ' ')
        else:
            print('\033[32m' + str(i + 1) + '\033[0m', end = '  ')
        for j in range(10):
            print(m[i][j].show, end = ' ')
        print()

def config(pos1, pos2):
    if m[pos1][pos2].inside != '0' and m[pos1][pos2].inside != '▶':
        m[pos1][pos2].show = m[pos1][pos2].inside
    elif m[pos1][pos2].inside == '▶':
        pass
    else:
        m[pos1][pos2].inside = ' '
        if pos1 == 0 and pos2 == 0:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1, pos2 + 1)
            config(pos1 + 1, pos2)
            config(pos1 + 1, pos2 + 1)
        elif pos1 == 0 and pos2 == 9:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1, pos2 - 1)
            config(pos1 + 1, pos2)
            config(pos1 + 1, pos2 - 1)
        elif pos1 == 9 and pos2 == 0:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1, pos2 + 1)
            config(pos1 - 1, pos2)
            config(pos1 - 1, pos2 + 1)
        elif pos1 == 9 and pos2 == 9:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1, pos2 - 1)
            config(pos1 - 1, pos2)
            config(pos1 - 1, pos2 - 1)
        elif pos1 == 0:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1, pos2 - 1)
            config(pos1, pos2 + 1)
            config(pos1 + 1, pos2 - 1)
            config(pos1 + 1, pos2)
            config(pos1 + 1, pos2 + 1)
        elif pos1 == 9:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1, pos2 - 1)
            config(pos1, pos2 + 1)
            config(pos1 - 1, pos2 - 1)
            config(pos1 - 1, pos2)
            config(pos1 - 1, pos2 + 1)
        elif pos2 == 0:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1 - 1, pos2)
            config(pos1 + 1, pos2)
            config(pos1 - 1, pos2 + 1)
            config(pos1, pos2 + 1)
            config(pos1 + 1, pos2 + 1)
        elif pos2 == 9:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1 - 1, pos2)
            config(pos1 + 1, pos2)
            config(pos1 - 1, pos2 - 1)
            config(pos1, pos2 - 1)
            config(pos1 + 1, pos2 - 1)
        else:
            m[pos1][pos2].show = m[pos1][pos2].inside
            config(pos1 - 1, pos2 - 1)
            config(pos1 - 1, pos2)
            config(pos1 - 1, pos2 + 1)
            config(pos1, pos2 - 1)
            config(pos1, pos2 + 1)
            config(pos1 + 1, pos2 - 1)
            config(pos1 + 1, pos2)
            config(pos1 + 1, pos2 + 1)

def debug():
    print('   \033[32m1 2 3 4 5 6 7 8 9 10\033[0m')
    for i in range(10):
        if i == 9:
            print('\033[32m10\033[0m', end = ' ')
        else:
            print('\033[32m' + str(i + 1) + '\033[0m', end = '  ')
        for j in range(10):
            print(m[i][j].inside, end = ' ')
        print()

ed = []

m = [[Mines() for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        m[i][j].show = '■'
        m[i][j].inside = '0'
for i in range(10):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    if (a, b) not in ed:
        m[a][b].inside = 'x'
        ed.append((a, b))
    else:
        i-=1

for i in range(10):
    for j in range(10):
        if m[i][j].inside == 'x':
            continue
        elif i == 0 and j == 0:
            if m[i][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif i == 0 and j == 9:
            if m[i][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif i == 9 and j == 0:
            if m[i][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif i == 9 and j == 9:
            if m[i][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif i == 0:
            if m[i][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif i == 9:
            if m[i][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif j == 0:
            if m[i - 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        elif j == 9:
            if m[i - 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
        else:
            if m[i - 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i - 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j - 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)
            if m[i + 1][j + 1].inside == 'x':
                m[i][j].inside = str(int(m[i][j].inside) + 1)

print('Welcome to Minesweeper!')
display()

while True:
    flag = not (bool(input('Do you want to flag a mine? ')))
    pos1 = int(input('Enter the row: '))
    pos2 = int(input('Enter the column: '))
    if flag:
        if m[pos1 - 1][pos2 - 1].inside == 'x':
            m[pos1 - 1][pos2 - 1].show = m[pos1 - 1][pos2 - 1].inside
            display()
            print('You lose!')
            break
        else:
            config(pos1 - 1, pos2 - 1)
            display()
    else:
        m[pos1 - 1][pos2 - 1].show = '▶'
        display()
        