from settings import *
import random

class Column:
    def __init__(self, **kwargs):
        properties = {
            "min_height": gameDefaultSettings["MIN_COLUMN_HEIGHT"],
            "max_height": gameDefaultSettings["MAX_COLUMN_HEIGHT"], 
            "position_x": gameDefaultSettings["WINDOW_WIDTH"],
            "column_image": gameDefaultSettings["COLUMN_IMAGE"],
            "rotated": False,
            "height": None,
        }
        setKwargsToProps(properties, kwargs)
        self.minHeight = properties["min_height"]
        self.maxHeight = properties["max_height"]
        self.columnImage = properties["column_image"]
        self.positionX = properties["position_x"]
        self.WIDTH = self.columnImage.get_width()
        self.HEIGHT = properties["height"] if properties["height"] else random.randint(self.minHeight, self.maxHeight)
        self.imageHeight = self.columnImage.get_height()
        self.positionY = 0
        self.rotated = properties["rotated"]
        if self.rotated:
            self.positionY = gameDefaultSettings["WINDOW_HEIGHT"] - self.HEIGHT
            self.columnImage = pygame.transform.rotate(self.columnImage, 180)

class Columns:
    def __init__(self, **kwargs):        
        properties = {
            "interface": None,
            "column_spacing": gameDefaultSettings["COLUMN_SPACING"],
            "columns": gameDefaultSettings["COLUMNS"]
        }
        setKwargsToProps(properties, kwargs)
        self.columnSpacing = properties["column_spacing"]
        self.spawns = properties["columns"]
        self.window = properties["interface"]
        newTopColumn = Column()
        newBottomColumn = Column(
            rotated=True,
            height=(self.window.HEIGHT-newTopColumn.HEIGHT-self.columnSpacing)
        )
        self.columns = [[newTopColumn, newBottomColumn, False], ]
        for i in range(self.spawns-1):          
            newColumnPosition = self.columns[-1][0].positionX+self.columns[-1][0].WIDTH+self.columnSpacing  
            newTopColumn = Column(
                position_x=newColumnPosition
            )
            newBottomColumn = Column(
                rotated=True, 
                position_x=newColumnPosition, 
                height=(self.window.HEIGHT-newTopColumn.HEIGHT-self.columnSpacing)
            )
            self.columns.append([newTopColumn, newBottomColumn, False])
    
    def addNewColumn(self):
        newColumnPosition = self.columns[-1][0].positionX+self.columns[-1][0].WIDTH+self.columnSpacing
        newTopColumn = Column(
            position_x=newColumnPosition
        )
        newBottomColumn = Column(
            rotated=True, 
            position_x=newColumnPosition, 
            height=(self.window.HEIGHT-newTopColumn.HEIGHT-self.columnSpacing)
        )
        self.columns.append([newTopColumn, newBottomColumn, False])
