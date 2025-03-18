###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################




mySprite = codesters.Sprite("dog.png")
def move_character(character, direction):
            if direction == "up":
                character.y -= character.speed
            elif direction == "down":
                character.y += character.speed
            elif direction == "left":
                character.x -= character.speed
            elif direction == "right":
                character.x += character.speed