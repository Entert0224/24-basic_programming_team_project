from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound
from Scenes import TeamSettingScene
from typing import Callable

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class StartScene(Scene) :
    question_mark : Sprite = None
    next_button : Callable[[Vec2, float, pygame.Color],bool] = None

    @classmethod
    def Setup(cls) :
        start_background = Sprite("assets/images/StartScene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))        
        cls.question_mark = Sprite("assets/images/question_mark.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 220), visible=False)        
        next_text = Sprite("assets/images/next_text.png",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))      
        cls.next_button = next_text.CreateButton()
    @classmethod
    def Update(cls) :
        if cls.next_button(Vec2(1.25,1.25)) :
            cls.question_mark.visible = True
            if Mouse.isDown() :
                Sound.PlaySound("click")
                Director.ChangeScene(TeamSettingScene)
        else :
            cls.question_mark.visible = False

    @classmethod
    def Exit(cls) :
        pass

