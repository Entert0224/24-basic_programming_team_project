from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Sound
from Scenes import TeamSettingScene, HowScene

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class StartScene(Scene) :
    question_mark : Sprite = None
    next_button = None
    how_to_play_button = None

    @classmethod
    def Setup(cls) :
        Sound.StopSound("BGM")
        Sound.PlaySound("BGM",True)
        start_background = Sprite("assets/images/StartScene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))        
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        cls.question_mark = Sprite("assets/images/question_mark.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 220), visible=False)        
        next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))      
        cls.next_button = next_text.CreateButton()

        how_to_play = Sprite("assets/images/how.png", Vec2(SCREEN_WIDTH/2 + 330, SCREEN_HEIGHT/2 + 260))
        cls.how_to_play_button = how_to_play.CreateButton()

    @classmethod
    def Update(cls) :
        if cls.next_button(Vec2(1.25,1.25)) :
            cls.question_mark.visible = True
            if Mouse.isDown() :
                Sound.PlaySound("click")
                Director.ChangeScene(TeamSettingScene)
        else :
            cls.question_mark.visible = False

        if cls.how_to_play_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                Director.ChangeScene(HowScene)

    @classmethod
    def Exit(cls) :
        pass

