from GameFramework import pygame, Vec2, Scene, Director, Mouse, Sprite, Text, Sound

SCREEN_WIDTH = Director.screen_width
SCREEN_HEIGHT = Director.screen_height

class HowScene(Scene) :
    back_button = None

    @classmethod
    def Setup(cls) :
        background = Sprite("assets/images/description_scene.jpg",Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))        
        AI_mark = Sprite("assets/images/AI_mark.png",Vec2(SCREEN_WIDTH/2 + 370, SCREEN_HEIGHT/2 - 270), scale=Vec2(0.1,0.1), layer=100)
        back_text = Sprite("assets/images/back_text.png",Vec2(SCREEN_WIDTH / 2 + 280, SCREEN_HEIGHT / 2 - 230), color=pygame.Color(0,0,0,255))      
        cls.back_button = back_text.CreateButton()

    @classmethod
    def Update(cls) :
        if cls.back_button(Vec2(1.25,1.25)) :
            if Mouse.isDown() :
                Sound.PlaySound("click")
                from Scenes import StartScene
                Director.ChangeScene(StartScene)

    @classmethod
    def Exit(cls) :
        pass

