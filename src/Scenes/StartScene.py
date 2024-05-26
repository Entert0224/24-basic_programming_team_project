from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite
from Scenes import GameScene

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class StartScene(Scene) :
    start_background: Sprite    = None
    question_mark   : Sprite    = None
    start_text      : Sprite    = None

    @classmethod
    def Setup(cls) :
        cls.start_background = Sprite("assets/images/StartScene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))        
        cls.question_mark = Sprite("assets/images/question_mark.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 220), visible=False)        
        cls.start_text = Sprite("assets/images/start_text.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))        


    @classmethod
    def Update(cls) :
        if cls.start_text.pointInRect(Mouse.GetMousePos()) :
            cls.start_text.scale = Vec2(1.25,1.25)
            cls.question_mark.visible = True
            if Mouse.isDown() :
                Director.ChangeScene(GameScene)
        else :
            cls.start_text.scale = Vec2(1,1)
            cls.question_mark.visible = False

    @classmethod
    def Exit(cls) :
        pass
