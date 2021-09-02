from settings import *

class Window:
    def __init__(self, **kwargs):
        self.frame = pygame.time.Clock()
        properties = {
            "width": gameDefaultSettings["WINDOW_WIDTH"],
            "height": gameDefaultSettings["WINDOW_HEIGHT"],
            "fps": gameDefaultSettings["FPS"],
            "title": gameDefaultSettings["WINDOW_TITLE"],
            "icon": gameDefaultSettings["ICON"],
            "background": gameDefaultSettings["BACKGROUND"],
            "speed": gameDefaultSettings["WINDOW_SPEED"]
        }
        setKwargsToProps(properties, kwargs)
        self.WIDTH = properties["width"]
        self.HEIGHT = properties["height"]
        self.title = properties["title"]
        self.FPS = properties["fps"]
        self.icon = properties["icon"]
        self.background = properties["background"]
        self.backgroundPosX = 0
        self.speed = properties["speed"]

        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

        self.interface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
