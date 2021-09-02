# Flappy Bird made by Thuongton999
# Ez-ist mode
from settings import *
from objects import *

def birdCollision(bird, column):
    return (
        bird.positionX < column.positionX + column.WIDTH and 
        bird.positionX + bird.WIDTH > column.positionX and 
        bird.positionY < column.positionY + column.HEIGHT and 
        bird.positionY + bird.HEIGHT > column.positionY
    )

window = Window()
bird = Bird()
environment = Environment()
columns = Columns(interface=window)
score = Score(interface=window)

def gameQuit():
    os.sys.exit("You dont want to play this game? Fvck you!")
    pygame.quit()

def gameStartScreen():
    startGame = False
    startButton = Button(
        position_x=window.WIDTH//2, 
        position_y=window.HEIGHT//2, 
        button_width=150, button_height=90
    )
    startButton.positionX -= startButton.WIDTH//2
    startButton.positionY -= startButton.HEIGHT//2
    while not startGame:
        window.interface.blit(window.background, (window.backgroundPosX, 0))
        window.interface.blit(window.background, (window.backgroundPosX+window.WIDTH, 0))
        window.backgroundPosX -= window.speed if window.backgroundPosX + window.WIDTH > 0 else -window.WIDTH
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()

        marginTop = 20
        marginBottom = 10
        titleRendered = bordered(
            "Flappy Peter Teo", 
            gameDefaultSettings["DEFAULT_TITLE"], 
            gfcolor=colors["white"], 
            ocolor=colors["clotting"],
            opx=5
        )
        header2Rendered = bordered(
            "thuongton999 code this, ya :))",
            gameDefaultSettings["DEFAULT_TEXT"],
            gfcolor=colors["sun"],
            ocolor=colors["white"],
            opx=3
        )
        copyrightRendered = bordered(
            "Copyright by thuongton999",
            gameDefaultSettings["COPYRIGHT"],
            gfcolor=colors["sun"],
            ocolor=colors["white"],
            opx=3
        )
        window.interface.blit(titleRendered, (window.WIDTH//2-titleRendered.get_width()//2, marginTop))
        window.interface.blit(header2Rendered, (window.WIDTH//2-header2Rendered.get_width()//2, marginTop*2+titleRendered.get_height()))
        window.interface.blit(
            copyrightRendered, 
            (window.WIDTH//2-copyrightRendered.get_width()//2, window.HEIGHT-marginBottom-copyrightRendered.get_height())
        )
        window.interface.blit(startButton.buttonImage, (startButton.positionX, startButton.positionY))
        mousePosX, mousePosY = pygame.mouse.get_pos()
        mouseButtonPressed = pygame.mouse.get_pressed(3)
        if startButton.onClick(mousePosX=mousePosX, mousePosY=mousePosY, clicked=mouseButtonPressed[0]):
            startGame = True
            break
        pygame.display.update()
        window.frame.tick(window.FPS)
    while startGame:
        bird.__init__()
        columns.__init__(interface=window)
        score.__init__(interface=window)

        getReady()
        gamePlay()
        startGame = gameOver()
    return startGame

def getReady():
    ready = False
    while not ready:
        window.interface.blit(window.background, (window.backgroundPosX, 0))
        window.interface.blit(window.background, (window.backgroundPosX+window.WIDTH, 0))
        window.backgroundPosX -= window.speed if window.backgroundPosX + window.WIDTH > 0 else -window.WIDTH
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                return

        marginLeft = 30
        getReadyTextRendered = bordered(
            "Get ready? Tap or press any key",
            gameDefaultSettings["DEFAULT_TEXT"],
            gfcolor=colors["grey"],
            ocolor=colors["white"],
            opx=3
        )
        window.interface.blit(bird.birdRotatedImage, (bird.positionX, bird.positionY))
        window.interface.blit(
            getReadyTextRendered, 
            (
                bird.positionX+bird.WIDTH+marginLeft, 
                bird.positionY+getReadyTextRendered.get_height()//2
            )
        )

        pygame.display.update()
        window.frame.tick(window.FPS)

def gamePlay():
    while not bird.dead:
        window.interface.blit(window.background, (window.backgroundPosX, 0))
        window.interface.blit(window.background, (window.backgroundPosX+window.WIDTH, 0))
        window.backgroundPosX -= window.speed if window.backgroundPosX + window.WIDTH > 0 else -window.WIDTH

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                environment.tapSound.play()
                bird.positionY -= bird.speed if bird.positionY >= 0 else 0
                bird.speed = bird.defaultSpeed
                            
        for topColumn, bottomColumn, passed in columns.columns:
            topColumn.positionX -= window.speed
            bottomColumn.positionX -= window.speed
            window.interface.blit(topColumn.columnImage, (topColumn.positionX, -(topColumn.imageHeight - topColumn.HEIGHT))) 
            window.interface.blit(bottomColumn.columnImage, (bottomColumn.positionX, bottomColumn.positionY))
            if birdCollision(bird, topColumn) or birdCollision(bird, bottomColumn):
                bird.dead = True
                break
        if columns.columns[0][0].positionX + columns.columns[0][0].WIDTH < bird.positionX and not columns.columns[0][2]:
            columns.columns[0][2] = True
            score.points += 1
        if columns.columns[0][0].positionX + columns.columns[0][0].WIDTH < 0:
            columns.columns.pop(0)
            columns.addNewColumn()

        bird.positionY += bird.speed + 0.5*environment.gravity
        bird.speed += environment.gravity
        bird.birdRotatedImage = pygame.transform.rotate(bird.birdDefaultImage, -bird.speed*2)
        
        bird.updateBirdSize()

        window.interface.blit(bird.birdRotatedImage, (bird.positionX, bird.positionY))
        score.render()

        if not (0 <= bird.positionY <= window.HEIGHT - bird.HEIGHT):
            bird.dead = True
  
        pygame.display.update()
        window.frame.tick(window.FPS)

def gameOver():
    environment.gameOverSound.play()
    scoreBoard = ScoreBoard(points=score.points, interface=window)
    titleRendered = bordered(
        "GAME OVER", 
        gameDefaultSettings["DEFAULT_TITLE"], 
        gfcolor=colors["white"], 
        ocolor=colors["clotting"],
        opx=5
    )
    cakhiaRendered = bordered(
        "You have been addicted xD",
        gameDefaultSettings["DEFAULT_TEXT"],
        gfcolor=colors["white"],
        ocolor=colors["clotting"],
        opx=3
    )
    notificationRendered = bordered(
        "Press SPACE to play again or ESC to go back to Menu",
        gameDefaultSettings["DEFAULT_TEXT"],
        gfcolor=colors["lemon_chiffon"],
        ocolor=colors["sun"],
        opx=3
    )
    titleDropDownSpeed = 6
    titlePositionX = window.WIDTH//2-titleRendered.get_width()//2
    titlePositionY = -titleRendered.get_height()
    titleHeight = titleRendered.get_height()
    marginBottom = 10
    marginTop = 20
    notificationPositionX = window.WIDTH//2-notificationRendered.get_width()//2
    notificationPositionY = scoreBoard.positionY+scoreBoard.HEIGHT+marginTop
    cakhiaPositionX = window.WIDTH//2-cakhiaRendered.get_width()//2
    cakhiaPositionY = scoreBoard.positionY-marginBottom-cakhiaRendered.get_height()
    
    playAgain = False
    while not playAgain:
        window.interface.blit(window.background, (window.backgroundPosX, 0))
        window.interface.blit(window.background, (window.backgroundPosX+window.WIDTH, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

        titlePositionY += titleDropDownSpeed if titlePositionY+titleHeight+marginBottom < cakhiaPositionY else 0
        
        window.interface.blit(cakhiaRendered, (cakhiaPositionX, cakhiaPositionY))
        window.interface.blit(notificationRendered, (notificationPositionX,notificationPositionY))
        window.interface.blit(titleRendered, (titlePositionX, titlePositionY))
        scoreBoard.renderScoreBoard()

        pygame.display.update()
        window.frame.tick(window.FPS)
    return playAgain
    

if __name__ == "__main__":
    os.system("cls")

    home = True
    while home:
        gameStartScreen()