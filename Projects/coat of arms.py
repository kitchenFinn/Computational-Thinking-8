###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################




q1 = codesters.Square(-100, -100, 200, 'black')
q2 = codesters.Square(100, 100, 200, 'white')
q3 = codesters.Square(-100, 100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'green')
q5 = codesters.Triangle(-100, -100, 145,'green')
q5.set_opacity(50)


stage.set_background("winter.png")
mySprite2 = codesters.Sprite("soccer.png", -100, 100)
mySprite1 = codesters.Sprite("hi.png", 100, -100)
mySprite1.say("DIlion Latham")
codesters.Sprite("SAAS.png", 100, 100)
codesters.Sprite("Sounders.png", -100, -100)
codesters.Text("FINN HART", 0, 220, "gold")