import pygame
import sys
import os
import pathlib

pygame.mixer.init()
pygame.init()

# this use for build .exe file
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = pathlib.Path(__file__).parent.resolve()
    return os.path.join(base_path, relative_path)

gameDefaultSettings = {
    "WINDOW_WIDTH": 1000,
    "WINDOW_HEIGHT": 600,
    "WINDOW_TITLE": "Flappy Peter Teo (Made by Thuongton999)",
    "BIRD_WIDTH": 100,
    "BIRD_HEIGHT": 80,
    "SPAWN_POSITION": (200, 255),
    "BIRD_JUMP_SPEED": -8,
    "WINDOW_SPEED": 3,
    "FPS": 60,
    "GRAVITY": 0.5,
    "MIN_COLUMN_HEIGHT": 100,
    "MAX_COLUMN_HEIGHT": 300,
    "COLUMN_SPACING": 250,
    "COLUMNS": 6,
    "DEFAULT_TEXT": pygame.font.Font(resource_path("font/FlappyBirdRegular.ttf"), 48),
    "DEFAULT_HEADER": pygame.font.Font(resource_path("font/FlappyBirdRegular.ttf"), 78),
    "DEFAULT_TITLE": pygame.font.Font(resource_path("font/FlappyBirdRegular.ttf"), 128),
    "COPYRIGHT": pygame.font.Font(resource_path("font/FlappyBirdRegular.ttf"), 42),
    "BIRD_IMAGE": pygame.image.load(resource_path("images/peter_teo.png")),
    "COLUMN_IMAGE": pygame.image.load(resource_path("images/dieucay.png")),
    "ICON": pygame.image.load(resource_path("images/favicon.ico")),
    "BACKGROUND": pygame.image.load(resource_path("images/background.png")),
    "SCOREBOARD": pygame.image.load(resource_path("images/scoreboard.png")),
    "START_BUTTON": pygame.image.load(resource_path("images/start_button.png")),
    "BRONZE_MEDAL": pygame.image.load(resource_path("images/medal_bronze.png")),
    "SILVER_MEDAL": pygame.image.load(resource_path("images/medal_silver.png")),
    "GOLD_MEDAL": pygame.image.load(resource_path("images/medal_gold.png")),
    "PlATINUM_MEDAL": pygame.image.load(resource_path("images/medal_platinum.png")),   
    "MEDAL_HOVER": pygame.image.load(resource_path("images/medal_hover.png")),
    "TAP_SOUND": pygame.mixer.Sound(resource_path("sounds/pop.wav")),
    "GAME_OVER_SOUND": pygame.mixer.Sound(resource_path("sounds/game_over.wav")),
}

colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "clotting": (82,58,74),
    "sun": (230, 193, 32),
    "grey": (143, 143, 143),
    "lemon_chiffon": (255, 250, 205),
}

def setKwargsToProps(props, kwargs):
    settings = kwargs.items()
    for setting, value in settings:
        try:
            props[setting] = value
        except KeyError:
            raise "Key setting %s not found" % (setting)

class Environment:
    def __init__(self, **kwargs):
        properties = {
            "gravity": gameDefaultSettings["GRAVITY"],
            "tap_sound": gameDefaultSettings["TAP_SOUND"],
            "game_over_sound": gameDefaultSettings["GAME_OVER_SOUND"]
        }
        setKwargsToProps(properties, kwargs)
        self.gravity = properties["gravity"]
        self.tapSound = properties["tap_sound"]
        self.gameOverSound = properties["game_over_sound"]