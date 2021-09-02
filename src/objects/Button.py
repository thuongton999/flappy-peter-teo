from settings import *

class Button:
    def __init__(self, **kwargs):
        properties = {
            "button_image": gameDefaultSettings["START_BUTTON"],
            "button_width": 100,
            "button_height": 60,
            "position_x": 100,
            "position_y": 100,
        }
        setKwargsToProps(properties, kwargs)
        self.WIDTH, self.HEIGHT = properties["button_width"], properties["button_height"]
        self.positionX, self.positionY = properties["position_x"], properties["position_y"]
        self.buttonImage = pygame.transform.scale(properties["button_image"], (self.WIDTH, self.HEIGHT))
    
    def onClick(self, **mouse):
        if mouse["clicked"]:
            return (
                self.positionX <= mouse["mousePosX"] <= self.positionX + self.WIDTH and
                self.positionY <= mouse["mousePosY"] <= self.positionY + self.HEIGHT
            )
        return False
