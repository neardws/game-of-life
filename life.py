import random

width = 10
height = 10
screen = []


def Init():
    global screen
    for i in range(height):
        line = []
        for j in range(width):
            if random.random() > 0.8:
                line.append('#')
            else:
                line.append(' ')
        screen.append(line)


def PrintScreen():
    global screen
    for i in range(height):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print('|')


def getScreen(i,j):
    return screen[i][j]


def GetNearbyCellsCount(i, j):
    global screen
    nearby = []
    if i > 0 and i < height - 1:
        if j > 0 and j < width - 1:
            nearby.append(getScreen(i - 1, j - 1))
            nearby.append(getScreen(i - 1, j))
            nearby.append(getScreen(i - 1, j + 1))
            nearby.append(getScreen(i, j - 1))
            nearby.append(getScreen(i, j + 1))
            nearby.append(getScreen(i + 1, j - 1))
            nearby.append(getScreen(i + 1, j))
            nearby.append(getScreen(i + 1, j + 1))
        elif j == 0:
            nearby.append(getScreen(i - 1, j))
            nearby.append(getScreen(i - 1, j + 1))
            nearby.append(getScreen(i, j + 1))
            nearby.append(getScreen(i + 1, j))
            nearby.append(getScreen(i + 1, j + 1))
        elif j == width - 1:
            nearby.append(getScreen(i - 1, j - 1))
            nearby.append(getScreen(i - 1, j))
            nearby.append(getScreen(i, j - 1))
            nearby.append(getScreen(i + 1, j - 1))
            nearby.append(getScreen(i + 1, j))
    elif i == 0:
        if j > 0 and j < width - 1:
            nearby.append(getScreen(i, j - 1))
            nearby.append(getScreen(i, j + 1))
            nearby.append(getScreen(i + 1, j - 1))
            nearby.append(getScreen(i + 1, j))
            nearby.append(getScreen(i + 1, j + 1))
        elif j == 0:
            nearby.append(getScreen(i, j + 1))
            nearby.append(getScreen(i + 1, j))
            nearby.append(getScreen(i + 1, j + 1))
        elif j == width - 1:
            nearby.append(getScreen(i, j - 1))
            nearby.append(getScreen(i + 1, j - 1))
            nearby.append(getScreen(i + 1, j))
    elif i == height -1:
        if j > 0 and j < width - 1:
            nearby.append(getScreen(i - 1, j - 1))
            nearby.append(getScreen(i - 1, j))
            nearby.append(getScreen(i - 1, j + 1))
            nearby.append(getScreen(i, j - 1))
            nearby.append(getScreen(i, j + 1))
        elif j == 0:
            nearby.append(getScreen(i - 1, j))
            nearby.append(getScreen(i - 1, j + 1))
            nearby.append(getScreen(i, j + 1))
        elif j == width - 1:
            nearby.append(getScreen(i - 1, j - 1))
            nearby.append(getScreen(i - 1, j))
            nearby.append(getScreen(i, j - 1))
    number = 0
    for i in nearby:
        if i == '#':
            number = number + 1
    return number


def Update():
    global screen
    newScreen = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(' ')
        newScreen.append(line)
    for i in range(height):
        for j in range(width):
            count = GetNearbyCellsCount(i, j)
            if count == 3:
                newScreen[i][j] = '#'
            elif count < 2 or count > 3:
                newScreen[i][j] = ' '
            else:
                newScreen[i][j] = screen[i][j]
    screen = newScreen

def Loop():
    Update()
    PrintScreen()


def Start():
    print('== Game of Life ==')
    print('Press any key...')
    input()
    Init()
    PrintScreen()
    c = input()
    while c != 'q':
        Loop()
        c = input()
    print('End')


if __name__ == "__main__":
    Start()
