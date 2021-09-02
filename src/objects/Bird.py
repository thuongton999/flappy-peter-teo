from settings import *

class Bird:
    def __init__(self, **kwargs):
        self.dead = False
        properties = {
            "width": gameDefaultSettings["BIRD_WIDTH"],
            "height": gameDefaultSettings["BIRD_HEIGHT"],
            "spawn_position": gameDefaultSettings["SPAWN_POSITION"],
            "speed": gameDefaultSettings["BIRD_JUMP_SPEED"],
            "bird_image": gameDefaultSettings["BIRD_IMAGE"],
            "default_speed": gameDefaultSettings["BIRD_JUMP_SPEED"]
        }
        setKwargsToProps(properties, kwargs)
        self.WIDTH = properties["width"]
        self.HEIGHT = properties["height"]
        self.positionX, self.positionY = properties["spawn_position"]
        self.defaultSpeed = properties["default_speed"]
        self.speed = properties["speed"]
        self.birdDefaultImage = pygame.transform.scale(properties["bird_image"], (self.WIDTH, self.HEIGHT))
        self.birdRotatedImage = self.birdDefaultImage

    def updateBirdSize(self):
        self.WIDTH = self.birdRotatedImage.get_width()
        self.HEIGHT = self.birdRotatedImage.get_height()
