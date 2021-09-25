import pygame

pygame.init()

screen = pygame.display.set_mode((700, 730))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill((0, 255, 0))

formated_screen = pygame.transform.scale(pygame.image.load("TicTacLoadingScreen.jpg"), (700, 700))
imagex = pygame.transform.scale(pygame.image.load("pngX.png"), (220, 220))
x_wins = pygame.transform.scale(pygame.image.load("XWins.jpg"), (700, 700))
o_wins = pygame.transform.scale(pygame.image.load("OWins.jpg"), (700, 700))
tie = pygame.transform.scale(pygame.image.load("tie.jpg"), (700, 700))

font = pygame.font.Font('freesansbold.ttf', 40)
font1 = pygame.font.Font('freesansbold.ttf', 25)
font2 = pygame.font.Font('freesansbold.ttf', 30)

draw_object = 'O'

filled = [False, False, False, False, False, False, False, False, False]
board = ['bs', 'bs', 'bs', 'bs', 'bs', 'bs', 'bs', 'bs', 'bs']
winx = 0
wino = 0


def check_winX():
    # check row
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or board[3] == 'X' and board[4] == 'X' and board[
        5] == 'X' or board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return True
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[
        7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return True
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or board[2] == 'X' and board[4] == 'X' and board[
        6] == 'X':
        return True
    else:
        return False


def check_winO():
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or board[3] == 'O' and board[4] == 'O' and board[
        5] == 'O' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return True
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or board[1] == 'O' and board[4] == 'O' and board[
        7] == 'O' or board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return True
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or board[2] == 'O' and board[4] == 'O' and board[
        6] == 'O':
        return True
    else:
        return False


def reset():
    for x in range(9):
        filled[x] = False
        board[x] = 'bs'


def endScreen(image):
    global winx
    global wino
    while (True):
        screen.blit(image, (0, 0))
        start = pygame.draw.rect(screen, (255, 204, 0), (275, 350, 150, 80), 5)
        screen.blit(font1.render("CONTINUE", True, (255, 204, 0)), (283, 375))
        quit = pygame.draw.rect(screen, (255, 204, 0), (275, 450, 150, 80), 5)
        screen.blit(font1.render("Quit", True, (255, 204, 0)), (315, 475))
        restart = pygame.draw.rect(screen, (255, 204, 0), (275, 550, 150, 80), 5)
        screen.blit(font1.render("RESTART", True, (255, 204, 0)), (290, 575))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (start.collidepoint((pos))):
                    reset()
                    return 0
                elif (quit.collidepoint((pos))):
                    pygame.quit()
                elif restart.collidepoint((pos)):
                    reset()
                    wino = 0
                    winx = 0
                    return 0
        pygame.display.update()


def game_loop():
    global wino
    global winx
    tiles = []
    screen.fill((255, 255, 255))
    posY = 10
    global draw_object
    owin = font2.render(("Player O: " + str(wino)), True, (255, 204, 0))
    screen.blit(owin, (20, 700))
    xwin = font2.render(("Player X: " + str(winx)), True, (255, 204, 0))
    screen.blit(xwin, (520, 700))

    for y in range(3):
        posX = 10
        for x in range(3):
            tiles.append(pygame.draw.rect(screen, (0, 255, 0), (posX, posY, 220, 220)))
            posX += 230
        posY += 230
    running = True
    while running:
        win = check_winX() or check_winO()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if not win:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    numTiles = 0
                    for tile in tiles:
                        if tile.collidepoint(pos) and not filled[numTiles] and draw_object == 'O':
                            pygame.draw.circle(screen, (0, 0, 0), (tile.x + 110, tile.y + 110), 100, 10)
                            draw_object = 'X'
                            filled[numTiles] = True
                            board[numTiles] = 'O'
                        elif tile.collidepoint(pos) and not filled[numTiles] and draw_object == 'X':
                            screen.blit(imagex, (tile.x, tile.y + 5))
                            draw_object = 'O'
                            filled[numTiles] = True
                            board[numTiles] = 'X'
                        numTiles += 1
            if win or 'bs' not in board:
                if check_winO():
                    wino += 1
                    draw_object = 'O'
                    endScreen(o_wins)
                    game_loop()
                elif check_winX():
                    winx += 1
                    draw_object = 'X'
                    endScreen(x_wins)
                    game_loop()
                else:
                    endScreen(tie)
                    game_loop()
        pygame.display.update()


def optionScreen():
    global draw_object
    while True:
        screen.blit(formated_screen, (0, 0))
        screen.blit(font1.render("WHICH PLAYER WOULD LIKE TO GO FIRST?", True, (255, 204, 0)), (90, 540))
        playO = pygame.draw.rect(screen, (255, 204, 0), (150, 600, 150, 90), 5)
        playX = pygame.draw.rect(screen, (255, 204, 0), (400, 600, 150, 90), 5)
        screen.blit(font2.render("PlayerO", True, (255, 204, 0)), (165, 630))
        screen.blit(font2.render("PlayerX", True, (255, 204, 0)), (415, 630))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos1 = pygame.mouse.get_pos()
                if playO.collidepoint(pos1):
                    draw_object = 'O'
                    return 0
                elif playX.collidepoint(pos1):
                    draw_object = 'X'
                    return 0
        pygame.display.update()


def enter_screen():
    run = True
    while (run):
        screen.blit(formated_screen, (0, 0))
        start = pygame.draw.rect(screen, (255, 204, 0), (275, 500, 150, 90), 5)
        text = font.render("PLAY", True, (255, 204, 0))
        screen.blit(text, (300, 525))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (start.collidepoint((pos))):
                    optionScreen()
                    return 0
        pygame.display.update()


enter_screen()
game_loop()

import pygame

pygame.init()

screen = pygame.display.set_mode((700, 730))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill((0, 255, 0))

formated_screen = pygame.transform.scale(pygame.image.load("TicTacLoadingScreen.jpg"), (700, 700))
imagex = pygame.transform.scale(pygame.image.load("pngX.png"), (220, 220))
x_wins = pygame.transform.scale(pygame.image.load("XWins.jpg"), (700, 700))
o_wins = pygame.transform.scale(pygame.image.load("OWins.jpg"), (700, 700))
tie = pygame.transform.scale(pygame.image.load("tie.jpg"), (700, 700))

font = pygame.font.Font('freesansbold.ttf', 40)
font1 = pygame.font.Font('freesansbold.ttf', 25)
font2 = pygame.font.Font('freesansbold.ttf', 30)

draw_object = 'O'

filled = [False, False, False, False, False, False, False, False, False]
board = ['bs', 'bs', 'bs', 'bs', 'bs', 'bs', 'bs', 'bs', 'bs']
winx = 0
wino = 0


def check_winX():
    # check row
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or board[3] == 'X' and board[4] == 'X' and board[
        5] == 'X' or board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return True
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[
        7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return True
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or board[2] == 'X' and board[4] == 'X' and board[
        6] == 'X':
        return True
    else:
        return False


def check_winO():
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or board[3] == 'O' and board[4] == 'O' and board[
        5] == 'O' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return True
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or board[1] == 'O' and board[4] == 'O' and board[
        7] == 'O' or board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return True
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or board[2] == 'O' and board[4] == 'O' and board[
        6] == 'O':
        return True
    else:
        return False


def reset():
    for x in range(9):
        filled[x] = False
        board[x] = 'bs'


def endScreen(image):
    global winx
    global wino
    while (True):
        screen.blit(image, (0, 0))
        start = pygame.draw.rect(screen, (255, 204, 0), (275, 350, 150, 80), 5)
        screen.blit(font1.render("CONTINUE", True, (255, 204, 0)), (283, 375))
        quit = pygame.draw.rect(screen, (255, 204, 0), (275, 450, 150, 80), 5)
        screen.blit(font1.render("Quit", True, (255, 204, 0)), (315, 475))
        restart = pygame.draw.rect(screen, (255, 204, 0), (275, 550, 150, 80), 5)
        screen.blit(font1.render("RESTART", True, (255, 204, 0)), (290, 575))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (start.collidepoint((pos))):
                    reset()
                    return 0
                elif (quit.collidepoint((pos))):
                    pygame.quit()
                elif restart.collidepoint((pos)):
                    reset()
                    wino = 0
                    winx = 0
                    return 0
        pygame.display.update()


def game_loop():
    global wino
    global winx
    tiles = []
    screen.fill((255, 255, 255))
    posY = 10
    global draw_object
    owin = font2.render(("Player O: " + str(wino)), True, (255, 204, 0))
    screen.blit(owin, (20, 700))
    xwin = font2.render(("Player X: " + str(winx)), True, (255, 204, 0))
    screen.blit(xwin, (520, 700))

    for y in range(3):
        posX = 10
        for x in range(3):
            tiles.append(pygame.draw.rect(screen, (0, 255, 0), (posX, posY, 220, 220)))
            posX += 230
        posY += 230
    running = True
    while running:
        win = check_winX() or check_winO()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if not win:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    numTiles = 0
                    for tile in tiles:
                        if tile.collidepoint(pos) and not filled[numTiles] and draw_object == 'O':
                            pygame.draw.circle(screen, (0, 0, 0), (tile.x + 110, tile.y + 110), 100, 10)
                            draw_object = 'X'
                            filled[numTiles] = True
                            board[numTiles] = 'O'
                        elif tile.collidepoint(pos) and not filled[numTiles] and draw_object == 'X':
                            screen.blit(imagex, (tile.x, tile.y + 5))
                            draw_object = 'O'
                            filled[numTiles] = True
                            board[numTiles] = 'X'
                        numTiles += 1
            if win or 'bs' not in board:
                if check_winO():
                    wino += 1
                    draw_object = 'O'
                    endScreen(o_wins)
                    game_loop()
                elif check_winX():
                    winx += 1
                    draw_object = 'X'
                    endScreen(x_wins)
                    game_loop()
                else:
                    endScreen(tie)
                    game_loop()
        pygame.display.update()


def optionScreen():
    global draw_object
    while True:
        screen.blit(formated_screen, (0, 0))
        screen.blit(font1.render("WHICH PLAYER WOULD LIKE TO GO FIRST?", True, (255, 204, 0)), (90, 540))
        playO = pygame.draw.rect(screen, (255, 204, 0), (150, 600, 150, 90), 5)
        playX = pygame.draw.rect(screen, (255, 204, 0), (400, 600, 150, 90), 5)
        screen.blit(font2.render("PlayerO", True, (255, 204, 0)), (165, 630))
        screen.blit(font2.render("PlayerX", True, (255, 204, 0)), (415, 630))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos1 = pygame.mouse.get_pos()
                if playO.collidepoint(pos1):
                    draw_object = 'O'
                    return 0
                elif playX.collidepoint(pos1):
                    draw_object = 'X'
                    return 0
        pygame.display.update()


def enter_screen():
    run = True
    while (run):
        screen.blit(formated_screen, (0, 0))
        start = pygame.draw.rect(screen, (255, 204, 0), (275, 500, 150, 90), 5)
        text = font.render("PLAY", True, (255, 204, 0))
        screen.blit(text, (300, 525))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (start.collidepoint((pos))):
                    optionScreen()
                    return 0
        pygame.display.update()


enter_screen()
game_loop()
