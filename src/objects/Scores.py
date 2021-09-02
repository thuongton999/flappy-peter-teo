from settings import *
from objects.Text import *

class Score:
    def __init__(self, **kwargs):
        properties = {
            "interface": None,
            "font": gameDefaultSettings["DEFAULT_HEADER"],
            "text_color": colors["white"],
            "border_color": colors["clotting"]
        }
        setKwargsToProps(properties, kwargs)
        self.interface = properties["interface"]
        self.font = properties["font"]
        self.color = properties["text_color"]
        self.borderColor = properties["border_color"]
        self.points = 0
    
    def render(self):
        scoredRendered = bordered(str(self.points), self.font, gfcolor=self.color, ocolor=self.borderColor)
        self.interface.interface.blit(scoredRendered, (self.interface.WIDTH//2 - scoredRendered.get_width()//2, 50))

class ScoreBoard():   
    def __init__(self, **kwargs):
        properties = {
            "points": 0,
            "position_x": 0,
            "position_y": 0,
            "width": 350,
            "height": 175,
            "interface": None,
            "board_image": gameDefaultSettings["SCOREBOARD"],
            "medal_hover": gameDefaultSettings["MEDAL_HOVER"],
            "medal_size": 80,
            "medals": {
                "bronze": gameDefaultSettings["BRONZE_MEDAL"],
                "silver": gameDefaultSettings["SILVER_MEDAL"],
                "gold": gameDefaultSettings["GOLD_MEDAL"],
                "platinum": gameDefaultSettings["PlATINUM_MEDAL"],
                "hover": gameDefaultSettings["MEDAL_HOVER"]
            }
        }
        setKwargsToProps(properties, kwargs)
        self.marginLeft = 30
        self.marginRight = 30
        self.marginTop = 20
        self.marginBottom = 20
        self.points = properties["points"]
        self.interface = properties["interface"]
        self.WIDTH = properties["width"]
        self.HEIGHT = properties["height"]
        self.positionX = properties["position_x"] if properties["position_x"] else self.interface.WIDTH//2-self.WIDTH//2
        self.positionY = properties["position_y"] if properties["position_y"] else self.interface.HEIGHT//2-self.HEIGHT//2
        self.medalSize = properties["medal_size"]
        self.medalPositionX = self.positionX + self.marginLeft
        self.medalPositionY = self.positionY + self.HEIGHT//2 - self.marginBottom
        self.medalHoverSize = self.medalSize + 6
        self.scoreBoardImage = pygame.transform.scale(properties["board_image"], (self.WIDTH, self.HEIGHT))
        self.medals = {
            "bronze": pygame.transform.scale(properties["medals"]["bronze"], (self.medalSize, self.medalSize)),
            "silver": pygame.transform.scale(properties["medals"]["silver"], (self.medalSize, self.medalSize)),
            "gold": pygame.transform.scale(properties["medals"]["gold"], (self.medalSize, self.medalSize)),
            "platinum": pygame.transform.scale(properties["medals"]["platinum"], (self.medalSize, self.medalSize)),
            "hover": pygame.transform.scale(properties["medals"]["hover"], (self.medalHoverSize, self.medalHoverSize))
        }
        self.medalReached = None
    
    def renderScoreBoard(self):
        self.interface.interface.blit(self.scoreBoardImage, (self.positionX, self.positionY))
        if self.points >= 5:
            self.medalReached = self.medals["bronze"]
            if self.points >= 10:
                self.medalReached = self.medals["silver"]
                if self.points >= 20:
                    self.medalReached = self.medals["gold"]
                    if self.points >= 40:
                        self.medalReached = self.medals["platinum"]
        medalTextRendered = bordered(
            "MEDAL",
            gameDefaultSettings["DEFAULT_TEXT"],
            gfcolor=colors["clotting"],
            ocolor=colors["lemon_chiffon"],
            opx=3
        )
        self.interface.interface.blit(
            medalTextRendered, 
            (
                self.positionX+self.marginLeft, 
                self.positionY+self.marginTop
            )
        )
        self.interface.interface.blit(self.medals["hover"], (self.medalPositionX, self.medalPositionY))
        if self.medalReached:
            self.interface.interface.blit(
                self.medalReached, 
                (
                    self.medalPositionX+(self.medalHoverSize-self.medalSize)//2, 
                    self.medalPositionY+(self.medalHoverSize-self.medalSize)//2
                )
            )
        scoreTextRendered = bordered(
            "SCORES",
            gameDefaultSettings["DEFAULT_TEXT"],
            gfcolor=colors["clotting"],
            ocolor=colors["lemon_chiffon"],
            opx=3
        )
        scoreTextRenderedWidth, scoreTextRenderedHeight = scoreTextRendered.get_size()
        scorePointsRendered = bordered(
            str(self.points),
            gameDefaultSettings["DEFAULT_HEADER"],
            gfcolor=colors["clotting"],
            ocolor=colors["lemon_chiffon"],
            opx=3
        )
        scorePointsRenderedWidth, scorePointsRenderedHeight = scorePointsRendered.get_size()        
        
        self.interface.interface.blit(
            scoreTextRendered,
            (
                self.positionX+self.WIDTH-self.marginRight-scoreTextRenderedWidth,
                self.positionY+self.marginTop
            )
        )
        self.interface.interface.blit(
            scorePointsRendered, 
            (
                self.positionX+self.WIDTH-self.marginRight-scoreTextRenderedWidth+(scoreTextRenderedWidth-scorePointsRenderedWidth)//2, 
                self.positionY+self.marginTop+scoreTextRenderedHeight+(self.medalHoverSize-scorePointsRenderedHeight)//2
            )
        )